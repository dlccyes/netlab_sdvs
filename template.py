import cv2
import argparse
import multiprocessing as mp
from collections import deque
from threading import Thread
import time

class strm:
    def __init__(self):
        self.buff = deque(maxlen = 1)
        self.doing = True
        # self.cap = None
        pipeline = (
            "nvarguscamerasrc ! "
                "video/x-raw(memory:NVMM), "
                "width=(int)1920, height=(int)1080, "
                "format=(string)NV12, framerate=(fraction)30/1 ! "
            "queue ! "
            "nvvidconv flip-method=2 ! "
                "video/x-raw, "
                "width=(int)1920, height=(int)1080, "
                "format=(string)BGRx, framerate=(fraction)30/1 ! "
            "videoconvert ! "
                "video/x-raw, format=(string)BGR ! "
            "appsink"
        )
        # Complete the function body
        self.cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

    def gstreamer_camera(self):
        # Use the provided pipeline to construct the video capture in opencv

        try:
            while True:
                print("new iter")
                ret, frame = self.cap.read()
                if not ret:
                    print("??????/")
                    self.doing = False
                    break
                # enqueue frame to buffer
                self.buff.appendleft(frame)
                print(time.strftime('%X'), frame.shape)

        except KeyboardInterrupt as e:
            print("fuck")
            self.cap.release()
        pass


    def gstreamer_rtmpstream(self):
        # Use the provided pipeline to construct the video writer in opencv
        pipeline = (
            "appsrc ! "
                "video/x-raw, format=(string)BGR ! "
            "queue ! "
            "videoconvert ! "
                "video/x-raw, format=RGBA ! "
            "nvvidconv ! "
            "nvv4l2h264enc bitrate=8000000 ! "
            "h264parse ! "
            "flvmux ! "
            'rtmpsink location="rtmp://localhost/rtmp/live live=1"'
        )
        # print(type(pipeline))
        # Complete the function body
        # fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        w = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        h = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        fps = self.cap.get(cv2.CAP_PROP_FPS)
        out = cv2.VideoWriter(pipeline, cv2.CAP_GSTREAMER, 0, float(fps), (int(w), int(h)))
        try:
            while self.cap.isOpened():
                if not self.doing:
                    break
                # if not len(q): continue
                # frame = q.get()
                if not len(self.buff): continue
                assert len(self.buff) <= 1
                print("doing")
                # frame = self.buff.pop(0)
                frame = self.buff.pop()
                B, G, R = cv2.split(frame)
                frame = cv2.merge([R, R, R])
                out.write(frame)
                print(time.strftime('%X'), frame.shape)
                # greystyle
                # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                out.write(frame)
        except:
            print("saf")
            pass
    # You can apply some simple computer vision algorithm here

    def start(self):
        self.receive_video_thread = Thread(target = self.gstreamer_camera)
        # self.receive_video_thread.setDaemon(True) # auto terminated with process
        self.receive_video_thread.start()

        self.save_video_thread = Thread(target = self.gstreamer_rtmpstream)
        # self.save_video_thread = Thread(target = self.test)
        # self.save_video_thread.setDaemon(True) # auto terminated with process
        self.save_video_thread.start()


if __name__ == '__main__':
    pls = strm()
    pls.start()


# Complelte the code

