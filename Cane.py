import cv2
import numpy as np
cap=cv2.VideoCapture(0)
cap.set(3,480)
cap.set(4,480) 
while(True):
    ret,frame= cap.read()
    size = frame.size
    imghsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    RED_MIN = np.array([145,0,0], np.uint8)
    RED_MAX = np.array([165, 255, 255], np.uint8)
    mask0=cv2.inRange(imghsv,RED_MIN,RED_MAX)
    dstr=mask0
    C = cv2.countNonZero(dstr)
    #c=int(((int(no_red))/ (640*480))*100)
    print(C)
    cv2.imshow('shuck',frame)
    cv2.imshow('shuck',dstr)
    if cv2.waitKey(100) & 0xFF == ord('e'):
        break
