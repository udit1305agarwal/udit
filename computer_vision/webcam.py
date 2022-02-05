from cv2 import VideoCapture
import cv2
cap = VideoCapture(0)
while True:
    status,frame= cap.read()
    if not status:
        print(status)
        break
    cv2.imshow('window',frame)

    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows
