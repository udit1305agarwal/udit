from cv2 import VideoCapture
import cv2
cap = VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Output.avi', fourcc, 60.0, (640, 480))
while True:
    status,frame= cap.read()
    if not status:
        print(status)
        break
    cv2.imshow('window',frame)
    out.write(frame)
    if cv2.waitKey(1) == 27:
        break
out.release()
cap.release()
cv2.destroyAllWindows
