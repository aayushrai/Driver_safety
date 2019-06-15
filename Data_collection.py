import cv2
import os

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    if ret:
        cv2.imshow("camera",frame)
        if cv2.waitKey(1) & 0xFF == 27:
              break
    else:
        print("camera not found")
cv2.destroyAllWindows()
cap.release()
    
