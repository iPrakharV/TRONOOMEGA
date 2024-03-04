# -*- coding: utf-8 -*-
"""
Created on Tue May  8 16:53:15 2018

@author: Lab
"""

import cv2
import numpy as np

def main():
   
    
    cap = cv2.VideoCapture(0)
    
    cap.set(3,256)
    cap.set(4,192)
    if cap.isOpened():
        ret, frame = cap.read()
        print(ret)
        print(frame)
        
    else:
        ret=False
        
    while ret:
        ret, frame=cap.read()
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        low = np.array([100,50,50])
        high = np.array([140,255,255])
        imask = cv2.inRange(hsv,low,high)
        #final = cv2.bitwise_and(frame,frame,mask=imask)
        edges=cv2.Canny(gray,70,100)#values for lines and edges
        cv2.imshow("masked",imask)
        lines = cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=3,minLineLength=3)
        for line in lines:
            x1,y1,x2,y2 = line[0]
            cv2.line(gray,(x1,y1),(x2,y2),(0,255,0),5)#(0,255,0)-colour of line in frame set to green, size of the line
        cv2.imshow("image mask",edges)
        cv2.imshow("original Feed",frame)
        cv2.imshow("hough lines",gray)
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyAllWindows()

         
if __name__ ==("__main__"):
        main()
       