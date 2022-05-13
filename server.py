import sdvs
import os
import os.path as osp
import sys
BUILD_DIR = osp.join(osp.dirname(osp.abspath(__file__)), "build/service/")
sys.path.insert(0, BUILD_DIR)
import argparse

import grpc
from concurrent import futures
import mode_pb2
import mode_pb2_grpc


class ModeChangerServicer(mode_pb2_grpc.ModeChangerServicer):

    def __init__(self):
        pass

    def Compute(self, request, context):
        mode = request.mode
        response = mode_pb2.ModeResponse()
        if mode in {'hand', 'object', 'face'}:
            response.result = f"changing mode to {mode}"
        elif mode == '0':
            response.result = "starting stream"
        else:
            response.result = "invalid mode"

        sdvs.main(mode)

        return response

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="0.0.0.0", type=str)
    parser.add_argument("--port", default=8080, type=int)
    args = vars(parser.parse_args())

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    servicer = ModeChangerServicer()
    mode_pb2_grpc.add_ModeChangerServicer_to_server(servicer, server)

    try:
        server.add_insecure_port(f"{args['ip']}:{args['port']}")
        server.start()
        print(f"Run gRPC Server at {args['ip']}:{args['port']}")
        server.wait_for_termination()
    except KeyboardInterrupt:
        pass
