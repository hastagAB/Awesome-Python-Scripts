import numpy as np
import argparse
import imutils
import time
import cv2
from imutils.video import VideoStream
from imutils.video import FPS

argParse = argparse.ArgumentParser()
argParse.add_argument("-p", "--prototxt", required=True,
                      help="path to Caffe's deploy.prototxt file")
argParse.add_argument("-m", "--model", required=True,
                      help="path to the pretrained Caffe model")
argParse.add_argument("-c", "--confidence", type=float, default=0.3,
                      help="Filtering for detections with weak confidence intervals")
args = vars(argParse.parse_args())

features = ["background", "aeroplane", "bicycle", "bird", "boat",
            "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
            "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
            "sofa", "train", "tvmonitor"]

colors = np.random.uniform(0, 255, size=(len(features), 3))

read_net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])
video_stream = VideoStream(src=0).start()
time.sleep(2.0)
frames_per_sec = FPS().start()

while True:
    frame = video_stream.read()
    frame = imutils.resize(frame, width=600)
    (h, w) = frame.shape[:2]
    blob_from_img = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
                                          0.007843, (300, 300), 127.5, swapRB=True)
    read_net.setInput(blob_from_img)
    detect = read_net.forward()

    for i in np.arange(0, detect.shape[2]):
        c_int = detect[0, 0, i, 2]
        if c_int > args["confidence"]:
            c_index = int(detect[0, 0, i, 1])
            box = detect[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startx, starty, endx, endy) = box.astype("int")
            label = "{}: {:.2f}%".format(features[c_index], c_int * 100)
            print("Object detected: ", label)
            cv2.rectangle(frame, (startx, starty), (endx, endy), colors[c_index], 2)

            if starty - 15 > 15:
                y = starty - 15
            else:
                y = starty + 15
            cv2.putText(frame, label, (startx, y), cv2.FONT_HERSHEY_PLAIN, 0.4, colors[c_index], 2)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == ord("w"):
        break

    frames_per_sec.update()

frames_per_sec.stop()

print("Time elapsed: {:.2f}".format(frames_per_sec.elapsed()))
print("FPS: {:.2f}".format(frames_per_sec.fps()))

cv2.destroyAllWindows()
video_stream.stop()
