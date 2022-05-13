import os
import os.path as osp
import sys
BUILD_DIR = osp.join(osp.dirname(osp.abspath(__file__)), "build/service/")
sys.path.insert(0, BUILD_DIR)
import argparse

import grpc
import mode_pb2
import mode_pb2_grpc

import subprocess

def main(args):
    host = f"{args['ip']}:{args['port']}"
    print(host)
    with grpc.insecure_channel(host) as channel:
        stub = mode_pb2_grpc.ModeChangerStub(channel)

        request = mode_pb2.ModeRequest()
        request.mode = args['mode']

        # stub.Compute(request)
        response = stub.Compute(request)
        print(response.result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="localhost")
    parser.add_argument("--port", type=int, default=8080)
    parser.add_argument("--mode", type=str, default=0)
    args = vars(parser.parse_args())
    main(args)
