import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    #cv2.imshow("Frame",frame)
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_blue = np.array([138, 86 , 0])
    upper_blue = np.array([121, 255, 255])
    mask= cv2.inRange(hsv, lower_blue, upper_blue)
    
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    key=cv2.waitkey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows

