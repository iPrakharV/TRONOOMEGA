import serial, time
import cv2
import numpy as np
import math
arduino = serial.Serial('COM3' ,9600)
cap = cv2.VideoCapture(1)
x1=0
x2=0
f=0
while(True):
    c2=0
    sum2=0
    sum1=0
    c1=0
    ret, frame = cap.read()
    if(f==0):
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
        if(c<1):
            f=1
    if(f==1):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurredimg = cv2.GaussianBlur(gray,(5,5),5)
        cannyimg = cv2.Canny(blurredimg,50,100)
        #ret,thresh = cv2.threshold(cannyimg,75,175,0)
        image , contours, hierarchy = cv2.findContours(cannyimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        finallimg= cv2.drawContours(frame,contours, -1,(0,255,0),35)
        for x in range(240,-1,-1):
            red,green,blue=finallimg[x,100]
            if red==0 and green==255 and blue==0 :
                sum1=sum1+x
                c1=c1+1
            #if c1>10:
                x1=int(sum1/c1)
        for xx in range(240,480):
            red1,green1,blue1=finallimg[xx,100]
            if red==0 and green==255 and blue==0 :
                sum2=sum2+xx
                c2=c2+1
            #if c2>10:
                x2=int(sum2/c2)
        cv2.line(finallimg,(x1,100),(x2,100),(255,0,0),2)
        cv2.line(finallimg,(480,0),(480,480),(0,0,255),2)
        #x3=int((x2-x1)/2)
        x3=int((x1+x2)*0.5)
        left=201-5
        right=201  +5
        cv2.circle(finallimg,(x3,100),5,(0,0,255),-1)
        if(x3>right):
            arduino.write("c".encode())
            #RIGHT
            print('right')
        elif(x3<left):
            arduino.write("b".encode())
            #LEFT
            print('left')
        else :
            arduino.write("a".encode())
            #FORWARD
            print('fuckward')    
        cv2.imshow('hyg' , finallimg)
        cv2.imshow('hyg1' , cannyimg)
        if cv2.waitKey(100) & 0xFF == ord('e'):
            break
        
cap.release()
cv2.destroyAllWindows()
 
