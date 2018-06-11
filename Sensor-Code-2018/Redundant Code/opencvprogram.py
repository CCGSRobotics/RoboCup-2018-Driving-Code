import cv2

camera = cv2.VideoCapture("/dev/stdin")

while 1:
    (grabbed, frame) = camera.read()
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
