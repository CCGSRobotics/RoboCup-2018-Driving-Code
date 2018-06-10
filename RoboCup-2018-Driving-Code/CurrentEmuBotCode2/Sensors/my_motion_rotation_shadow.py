from collections import deque
import numpy as np
import argparse
import cv2
import imutils

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-r", "--real", type=str, default="real",
	help="real image or mask")

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

# keep looping
(grabbed, lastFrame) = camera.read()
count = 0
while True:
        count += 1
	# grab the current frame
	(grabbed, frame) = camera.read()
 
	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if args.get("video") and not grabbed:
		break
        mask = cv2.inRange(frame, (0,0,0), (0,0,0))
	mask = cv2.absdiff(frame, lastFrame, None)
	mask = cv2.erode(mask, None, iterations=1)
	
	resized = imutils.resize(mask, width=1024)
	ratio = mask.shape[0]/float(resized.shape[0])
	gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (5,5),0)
	thresh = cv2.threshold(blurred, 60,255,cv2.THRESH_BINARY)[1]

	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        try:
            if count % 2 == 0:
                for c in cnts:
                    M = cv2.moments(c)
                    cX = int((M['m10']/M['m00'])*ratio)
                    cY = int((M['m01']/M['m00'])*ratio)

                    c = c.astype('float')
                    c *= ratio
                    c = c.astype('int')
                    cv2.drawContours(frame, [c], -1, (0,255,0), 2)
            
        except:
            pass
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
        lastFrame = frame
# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
