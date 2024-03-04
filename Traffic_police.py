import cv2
import numpy as np
cap=cv2.VideoCapture(1)
cap.set(3,480)
cap.set(4,480) 
while(True):
    ret,frame= cap.read()
    size = frame.size
    imghsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    RED_MIN = np.array([0,50,50], np.uint8)
    RED_MAX = np.array([10, 255, 255], np.uint8)
    mask0=cv2.inRange(imghsv,RED_MIN,RED_MAX)
    lowwerred = np.array([170,50,50])
    uppperred = np.array([180,255,255])
    mask1=cv2.inRange(imghsv,lowwerred,uppperred)
    dstr=mask0 +mask1
    no_red = cv2.countNonZero(dstr)
    c=int(((int(no_red))/ (640*480))*100)
    print(c)
    cv2.imshow('fuck',frame)
    cv2.imshow('fuck',dstr)
    if cv2.waitKey(100) & 0xFF == ord('e'):
        break
