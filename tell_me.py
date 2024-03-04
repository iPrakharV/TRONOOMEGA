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
        
        #blue
        low = np.array([100,50,50])
        high = np.array([140,255,255])
        imask = cv2.inRange(hsv,low,high)
        final = cv2.bitwise_and(frame,frame,mask=imask)
        
        cv2.imshow("masked",final)
        cv2.imshow("image mask",imask)
        cv2.imshow("original Feed",frame)
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyAllWindows()

         
if __name__ ==("__main__"):
        main()
       