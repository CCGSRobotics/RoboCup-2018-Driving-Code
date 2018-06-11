from collections import deque
import numpy as np
import argparse
import imutils
import cv2



def Haz2(template):
    result = cv2.matchTemplate(frame, template, cv2.TM_CCORR_NORMED)
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
def Haz(camera):
    Oxi = cv2.imread('Oxidizer.png')
    Oxi = imutils.resize(Oxi, width=50)
    count = 0
    print(type(camera))
    # keep looping
    while True:
            # grab the current frame
            (grabbed, frame) = camera.read()
     
            # if we are viewing a video and we did not grab a frame,
            # then we have reached the end of the video
            if not grabbed:
                    break
            frame = Haz(Oxi)
            
            # show the frame to our screen
            cv2.imshow("Frame", frame)
            
            key = cv2.waitKey(1) & 0xFF
     
            # if the 'q' key is pressed, stop the loop
            if key == ord("q"):
                    break

def RotateReal(camera, pts, real):
    (grabbed, img) = camera.read()
    print(type(camera))
    while True:
            # grab the current frame
            (grabbed, frame) = camera.read()
            orgFrame = frame
            # if we are viewing a video and we did not grab a frame,
            # then we have reached the end of the video
            if not grabbed:
                    break

            mask = cv2.inRange(frame, (0,0,0), (0,0,0))
            mask = cv2.absdiff(frame, img, None)
            orgMask = mask

            mask = imutils.resize(mask, width=600)
            hsv = cv2.cvtColor(mask, cv2.COLOR_BGR2HSV)
     
            # construct a mask for the color "green", then perform
            # a series of dilations and erosions to remove any small
            # blobs left in the mask
            newMask = cv2.inRange(hsv, (0,0,10), (255,255,255))
            newMask = cv2.erode(newMask, None, iterations=2)
            newMask = cv2.dilate(newMask, None, iterations=2)
            
            # find contours in the mask and initialize the current
            # (x, y) center of the ball
            cnts = cv2.findContours(newMask.copy(), cv2.RETR_EXTERNAL,
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
                    cv2.imshow("orginal", frame)
            elif real == "mask":
                cv2.imshow("mask",mask)
            elif real == "rm":
                  cv2.imshow("mask",mask)
                  cv2.imshow("original", frame)
                
            key = cv2.waitKey(1) & 0xFF

            # if the 'q' key is pressed, stop the loop
            if key == ord("q"):
                    break
            img = orgFrame
