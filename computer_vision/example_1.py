import cv2
img = cv2.imread("C:/Users/DELL/OneDrive/Pictures/Screenshots/2022-01-19.png")
print('the image has',img.size,'pixels')
cv2.imshow('output',img)
cv2.imshow('output2',img/3)
cv2.waitKey(0)
