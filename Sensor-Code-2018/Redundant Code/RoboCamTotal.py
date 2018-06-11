from collections import deque
import numpy as np
import argparse
import imutils
import cv2
from RoboCamDef import *


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-r", "--real", type=str, default="real",
	help="real image or mask")
ap.add_argument("-b", "--buffer", type=int, default=0,
	help="max buffer size")

args = vars(ap.parse_args())
real = args.get("real")

raspi = True

pts = deque(maxlen=args["buffer"])
 
# if a video path was not supplied, grab the reference
# to the webcam
if not args.get("video", False):
    if raspi:
        camera = cv2.VideoCapture("/dev/stdin")
        print("raspi")
    else:
	camera = cv2.VideoCapture(0)
# otherwise, grab a reference to the video file
else:
	camera = cv2.VideoCapture(args["video"])
RotateReal(camera, pts, real)
a = raw_input()
while a != '':
    if a == "rotate":
       RotateReal(camera, pts, real)
    if a == "haz":
       Haz(camera)
    a = raw_input()
