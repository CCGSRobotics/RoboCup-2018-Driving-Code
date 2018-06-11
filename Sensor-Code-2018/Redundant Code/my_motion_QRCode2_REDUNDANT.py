'''
my_motion_QRCode2.py

Reads a QR code from a given image.
Based off the code from SART (https://github.com/SFXRescue/SARTRobot/blob/master/current/python/qr-read.py)

By Nick Patrikeos on 17DEC17

NOT WORKING
REDUNDANT
'''


import cv2
import numpy as np
from pyzbar.pyzbar import decode
import imutils
import argparse

def getNumber(line, prop):
    numbers = []
    count = 0
    found_equal = False

    if prop in line:
        for char in line:
            if found_equal:
                numbers.append(line[count])
            if char == 'b':
                found_equal = True
            if char == "'" and line[count + 1] == ",":
                return numbers

            count += 1
        return numbers

def dataArrayToString(line, prop):
    number_string = ""
    number = getNumber(line, prop)

    if number is None:
        return "No data found"
    
    for num in number:
        number_string += num
    return number_string

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

while True:
    (grabbed, frame) = camera.read()
    cv2img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    contrast_image = cv2.equalizeHist(frame)
    decoded = str(decode(contrast_image))
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(contrast_image, dataArrayToString(decoded, "data="),
                (50, 60), font, 1, (200, 255, 155), 2, cv2.LINE_AA)
    print(decoded)
    print(dataArrayToString(decoded, "data="))

    cv2.imshow('Keypoints', im)
    cv2.imshow('Contrasted', contrast_image)

    key = cv2.waitKey(1) & 0xFF
 
    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
            break

camera.release()
cv2.destroyAllWindows()

    
