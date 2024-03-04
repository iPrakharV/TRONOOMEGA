import cv2
import numpy as np
import math
cap = cv2.VideoCapture(1)
cap.set(3,480)
cap.set(4,480)
x1=0
x2=0
while(True):
    
    c2=0
    sum2=0
    sum1=0
    
    c1=0
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurredimg = cv2.GaussianBlur(gray,(5,5),5)
    cannyimg = cv2.Canny(blurredimg,25 ,150)
    #ret,thresh = cv2.threshold(cannyimg,125,255,0)
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
    #x3=int((x2-x1)/2)
    x3=int((x1+x2)*0.5)
    cv2.circle(finallimg,(x3,100),5,(0,0,255),-1)
    cv2.line(finallimg,(x1,100),(x2,100),(255,0,0),2)
    cv2.line(finallimg,(480,0),(480,480),(0,0,255),2)
    print(x3)
    
    
    cv2.imshow('hyg' , finallimg)
    cv2.imshow('hyg1' , cannyimg)
    if cv2.waitKey(100) & 0xFF == ord('e'):
        break
    
cap.release()
cv2.destroyAllWindows()
 
