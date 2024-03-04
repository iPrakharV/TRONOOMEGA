# -*- coding: utf-8 -*-
"""
Created on Tue May  8 16:53:15 2018

@author: Lab
"""

import cv2
import numpy as np

def main():
   
    
    cap = cv2.VideoCapture(1)
    
    cap.set(3,256)
    cap.set(4,192)
    if cap.isOpened():
        ret, frame = cap.read()
        
        
        
    else:
        ret=False
        
    while True:
        ret, frame=cap.read()
        #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #
        #edges=cv2.Canny(blur,75,150)
        #cv2.imshow("masked",final)
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        blur=cv2.GaussianBlur(hsv,(5,5),10)
        low = np.array([100,50,50])
        high = np.array([140,255,255])
        imask=cv2.inRange(blur,low,high)
        mask=cv2.Canny(frame,75,180)
        re, contours,pe =cv2.findContours(imask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#        cv2.drawContours(frame,contours,-1,(0,255,0),3)
        
        for contour in contours:
            area=cv2.contourArea(contour)
            if area>5000:
                cv2.drawContours(frame,contours,-1,(0,255,0),3)
        cv2.imshow("image mask",mask)
        cv2.imshow("original Feed",frame)
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyAllWindows()

         
if __name__ ==("__main__"):
        main()
       