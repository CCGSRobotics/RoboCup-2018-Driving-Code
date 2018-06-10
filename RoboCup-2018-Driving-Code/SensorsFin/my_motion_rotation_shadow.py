from collections import deque
import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-r", "--real", type=str, default="mask",
	help="real image or mask")

args = vars(ap.parse_args())
real = args.get("real")

raspi = True
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
(grabbed, img) = camera.read()
while True:
	# grab the current frame
	(grabbed, frame) = camera.read()
 
	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if args.get("video") and not grabbed:
		break

	mask = cv2.inRange(frame, (0,0,0), (0,0,0))
	mask = cv2.absdiff(frame, img, None)
	mask = cv2.erode(mask, None, iterations=1)

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
        img = frame
# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
