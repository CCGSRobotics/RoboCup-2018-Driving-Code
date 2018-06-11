#code based on example found at:
#http://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/
# import the necessary packages
from collections import deque
import numpy as np
import argparse
import imutils
import cv2
import time as t

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=32,
	help="max buffer size")
ap.add_argument("-r", "--real", type=str, default="real",
	help="real image or mask")
ap.add_argument("-t", "--type", type=str, default="blank",
	help="type of find")
args = vars(ap.parse_args())
real = args.get("real")
typ = args.get("type")

raspi = False

if typ == "blank":
    greenLower = (0, 0, 0)
    greenUpper = (0, 0, 0)
elif typ == "BD":
    greenLower = (71, 32, 37)
    greenUpper = (203, 67, 65)
elif typ == "Servo":
    greenLower = (72, 80, 26)
    greenUpper = (140, 165, 142)
elif typ == "ppbo":
    greenLower = (14, 20, 157)
    greenUpper = (40, 228, 246)
elif typ == "TAC":
    greenLower = (0, 16, 46)
    greenUpper = (183, 170, 105)
elif typ == "bby":
    greenLower = (17,121,76)
    greenUpper = (52,228,218)
elif typ == "plier":
    greenLower = (73,108,78)
    greenUpper = (100,201,149)
elif typ == "bluey":
    greenLower = (108,222,155)
    greenUpper = (126,245,234)

#my eyes(broken)
#greenLower = (106, 84, 38)
#greenUpper = (138, 143, 55)

pts = deque(maxlen=args["buffer"])
 
# if a video path was not supplied, grab the reference
# to the webcam
if not args.get("video", False):
    if raspi:
        camera = cv2.VideoCapture("/dev/stdin")
    else:
	camera = cv2.VideoCapture(0)
 
# otherwise, grab a reference to the video file
else:
	camera = cv2.VideoCapture(args["video"])

# keep looping
while True:
	# grab the current frame
	(grabbed, frame) = camera.read()
 
	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if args.get("video") and not grabbed:
		break
 
	# resize the frame, blur it, and convert it to the HSV
	# color space
	frame = imutils.resize(frame, width=600)
	# blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 
	# construct a mask for the color "green", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
	mask = cv2.inRange(hsv, greenLower, greenUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
	# find contours in the mask and initialize the current
	# (x, y) center of the ball
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)[-2]
	center = None
 
	# only proceed if at least one contour was found
	if len(cnts) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
 
		# only proceed if the radius meets a minimum size
		if radius > 10:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
			cv2.circle(frame, (int(x), int(y)), int(radius),
				(0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)
 
	# update the points queue
	pts.appendleft(center)
	# loop over the set of tracked points
	for i in xrange(1, len(pts)):
		# if either of the tracked points are None, ignore
		# them
		if pts[i - 1] is None or pts[i] is None:
			continue
 
		# otherwise, compute the thickness of the line and
		# draw the connecting lines
		thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
		cv2.line(frame, pts[i - 1], pts[i], (0, 0, 0), thickness)
 
	# show the frame to our screen
	if real == "real":
        	cv2.imshow("Frame", frame)
        elif real == "mask":
            cv2.imshow("Frame",mask)
        else:
            cv2.imshow("Frame",hsv)
	key = cv2.waitKey(1) & 0xFF
 
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break
	#t.sleep(0.1)
 
# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
