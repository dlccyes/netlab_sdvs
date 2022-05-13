import cv2
import argparse
import multiprocessing as mp
from collections import deque
from threading import Thread
import time
import mediapipe as mpp

mp_drawing = mpp.solutions.drawing_utils
# face
mp_face_detection = mpp.solutions.face_detection
# object
mp_object_detection = mpp.solutions.object_detection
# hand
mp_hands = mpp.solutions.hands
mp_drawing_styles = mpp.solutions.drawing_styles

class strm:
    def __init__(self):
        self.buff = deque(maxlen = 1)
        self.doing = True
        # self.cap = None
        pipeline = (
            "nvarguscamerasrc ! "
                "video/x-raw(memory:NVMM), "
                "width=(int)1280, height=(int)720, "
                "format=(string)NV12, framerate=(fraction)30/1 ! "
            "queue ! "
            "nvvidconv flip-method=2 ! "
                "video/x-raw, "
                "width=(int)1280, height=(int)720, "
                "format=(string)BGRx, framerate=(fraction)30/1 ! "
            "videoconvert ! "
                "video/x-raw, format=(string)BGR ! "
            "appsink"
        )
        self.cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

    def gstreamer_camera(self):
        # Use the provided pipeline to construct the video capture in opencv

        try:
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    print("Stop!!!")
                    self.doing = False
                    break
                # print("Getting frame")
                # enqueue frame to buffer
                self.buff.appendleft(frame)

        except KeyboardInterrupt as e:
            print("Force stop!!!")
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
        w = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        h = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        fps = self.cap.get(cv2.CAP_PROP_FPS)
        out = cv2.VideoWriter(pipeline, cv2.CAP_GSTREAMER, 0, float(fps), (int(w), int(h)))
        while self.cap.isOpened():
            try:
                if not self.doing:
                    break
                if not len(self.buff): continue
                assert len(self.buff) <= 1
                # print("Writing frame")
                frame = self.buff.pop()
                mode = None
                # read mode from file
                with open("mode.txt", 'r') as m:
                    mode = m.readline().strip()

                if mode == "grey":
                    B, G, R = cv2.split(frame)
                    frame = cv2.merge([R, R, R])
                elif mode == "face":
                    with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
                        results = face_detection.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                elif mode == "object":
                    with mp_object_detection.ObjectDetection(min_detection_confidence=0.1) as object_detection:
                        results = object_detection.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                elif mode == "hand":
                    with mp_hands.Hands(
                        min_detection_confidence=0.5,
                        min_tracking_confidence=0.5) as hands:
                        results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                if mode in {'face', 'object'}:
                    if results.detections: # for face & object
                        for detection in results.detections:
                            mp_drawing.draw_detection(frame, detection)
                elif mode in {'hand'}:
                    if results.multi_hand_landmarks: # for hand
                        for hand_landmarks in results.multi_hand_landmarks:
                            mp_drawing.draw_landmarks(
                                frame,
                                hand_landmarks,
                                mp_hands.HAND_CONNECTIONS,
                                mp_drawing_styles.get_default_hand_landmarks_style(),
                                mp_drawing_styles.get_default_hand_connections_style())
                            
                out.write(frame)
            except Exception as e:
                print("error when writing")
                print(e)

    def start(self):
        self.receive_video_thread = Thread(target = self.gstreamer_camera)
        self.receive_video_thread.start()

        self.save_video_thread = Thread(target = self.gstreamer_rtmpstream)
        self.save_video_thread.start()

def main(mode=None):
    # write mode into a file for future access
    with open("mode.txt", 'w') as m:
        m.write(mode)

    # mode = 0 -> start
    if mode == '0':
        stream = strm()
        stream.start()

    print("haha")

if __name__ == '__main__':
    main('0')