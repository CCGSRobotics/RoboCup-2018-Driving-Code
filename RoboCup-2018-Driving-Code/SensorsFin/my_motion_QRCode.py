#installed zbar with difficulty, main steps taken from https://github.com/NaturalHistoryMuseum/gouda
#what worked for me (executed from anaconda command prompt)
#conda update --all
#conda update --all
#python -m pip install --upgrade pip
#python <Anaconda dir>\Scripts\pywin32_postinstall.py -install
#python -m pip install pathlib
#python -m pip install numpy
#python -m pip install Pillow
#conda install -c menpo opencv
#python -m pip install https://github.com/NaturalHistoryMuseum/zbar-python-patched/releases/download/v0.10/zbar-0.10-cp27-none-win32.whl

import cv2
import zbar
from PIL import Image
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-r", "--real", type=str, default="real",
	help="real image or mask")

args = vars(ap.parse_args())
real = args.get("real")

raspi = True

cv2.namedWindow("Frame")
# if a video path was not supplied, grab the reference
# to the webcam
if not args.get("video", False):
    print('sfkgljsflgk')
    if raspi:
        camera = cv2.VideoCapture("/dev/stdin")
    else:
	camera = cv2.VideoCapture(0)
# otherwise, grab a reference to the video file
else:
	camera = cv2.VideoCapture(args["video"])

scanner = zbar.ImageScanner()
scanner.parse_config('enable')

# Capture frames from the camera
while True:
    ret, output = camera.read()
    if not ret:
	  continue
    gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY, dstCn=0)
    pil = Image.fromarray(gray)
    width, height = pil.size
    raw = pil.tobytes()
    image = zbar.Image(width, height, 'Y800', raw)
    scanner.scan(image)
	
    for symbol in image:
        print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data

    cv2.imshow("Frame", output)

    # clear stream for next frame
    #rawCapture.truncate(0)

    # Wait for the magic key
    keypress = cv2.waitKey(1) & 0xFF
    if keypress == ord('q'):
    	break

# When everything is done, release the capture
camera.release()
cv2.destroyAllWindows()
