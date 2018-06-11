# import the necessary packages
from collections import deque
import numpy as np
import argparse
import imutils
import cv2

'''
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
args = vars(ap.parse_args())
'''

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-r", "--real", type=str, default="real",
	help="real image or mask")
ap.add_argument("-b", "--buffer", type=int, default=0,
	help="max buffer size")

args = vars(ap.parse_args())
real = args.get("real")

raspi = False

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
	
template = cv2.cvtColor(cv2.imread('Oxidizer.png'), cv2.COLOR_BGR2GRAY)
template = imutils.resize(template, width=50)
count = 0
# keep looping
while True:
	# grab the current frame
	(grabbed, frame) = camera.read()
        
	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if args.get("video") and not grabbed:
		break
        result = cv2.matchTemplate(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), template, cv2.TM_CCORR_NORMED)
        minmaxs = cv2.minMaxLoc(result)
        mins, maxs, min_pos, max_pos = minmaxs
        if maxs > 0.907:
            if count == 10:
                corner1 = max_pos
                corner2 = (corner1[0]+template.shape[1],corner1[1]+template.shape[0])
                cv2.rectangle(frame, corner1, corner2, (0,255,0),5)
                print(maxs,max_pos)
            else:
                    count += 1
        else:
                count = 0
        
	# show the frame to our screen
	cv2.imshow("Frame", frame)
        
	key = cv2.waitKey(1) & 0xFF
 
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break
 
# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
