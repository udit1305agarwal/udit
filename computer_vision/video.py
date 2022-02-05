import cv2
cap = cv2.VideoCapture('C:/Users/DELL/Downloads/WhatsApp Video 2022-01-31 at 7.31.44 PM.mp4')
while True:
    status, frame = cap.read()
    h,w,_ = frame.shape
    if not status:
        print("Status is missing")
        break
    frame_sm = cv2.resize(frame,(w//2,h//2))
    cv2.imshow("Output" ,frame)
    if cv2.waitKey(1) == '27':
        break
cap.release()
cv2.destroyAllWindows()
