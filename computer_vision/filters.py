from cv2 import VideoCapture
import numpy as np
import cv2
cap = VideoCapture(0)
while True:
    status,frame= cap.read()

    if not status:
        print(status)
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BAYER_BG2BGR)
    rgb = cv2.cvtColor(frame,cv2.COLOR_BAYER_BG2BGR_EA)
    cv2.imshow('window',frame)
    cv2.imshow('gray',gray)
    merged = np.hstack((frame,rgb))
    cv2.imshow("merged",merged)
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows
