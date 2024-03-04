import cv2
import numpy as np
import math
cap = cv2.VideoCapture(1)

while(True):
    x1=0
    c2=0
    sum2=0
    sum1=0
    x2=0
    c1=0
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurredimg = cv2.GaussianBlur(gray,(5,5),5)
    cannyimg = cv2.Canny(blurredimg,75,150)
    ret,thresh = cv2.threshold(cannyimg,127,255,0)
    image , contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    finallimg= cv2.drawContours(frame,contours, -1,(0,255,0),35)
    
    for x in range(240,-1,-1):
        #print('x=')
        #print(x)
        #print('----------')
        red,green,blue=finallimg[x,100]
        #print('r=')
        #print(red)
        #print('g=')
        #print(green)
        #print('b=')
        #print(blue)
        if red==0 and green==255 and blue==0 :
            #x1=x
            sum1=sum1+x
            c1=c1+1
            
            #print('x1=')
            #print(x)
            #print('---------')
            #break
        #if c1>10:
            x1=int(sum1/c1)
    for xx in range(240,480):
        
        #print('xx=')
        #print(xx)
        
        red1,green1,blue1=finallimg[xx,100]
        #print('r=')
        #print(red1)
        #print('g=')
        #print(green1)
        #print('b=')
        #print(blue1)
        if red==0 and green==255 and blue==0 :
            #x2=xx
            #x2=xx
            sum2=sum2+xx
            c2=c2+1
        #if c2>10:
            x2=int(sum2/c2)

            #print('x2=')
            #print(x2)
            #print('-------------')
            
    #print('-------------')
    #print('-------------')
    #print('x1=')
    #print(x1)
    #print('-------------')
    #print('-------------')
    ##print('x2=')
    ###print(x2
    #print('-------------')
    #print('-------------')
    cv2.line(finallimg,(x1,100),(x2,100),(255,0,0),2)
    cv2.line(finallimg,(480,0),(480,480),(0,0,255),2)
    x3=int((x2-x1)/2)
    cv2.circle(finallimg,(x3,100),5,(0,0,255),-1)
    cv2.imshow('hyg' , finallimg)
    cv2.imshow('hyg1' , cannyimg)
    if cv2.waitKey(100) & 0xFF == ord('e'):
        break
    
cap.release()
cv2.destroyAllWindows()
