import cv2

def main():
    windowName="Live Feed"
    cv2.namedWindow("Live Feed")
    
    cap = cv2.VideoCapture(0)
    
    
   
       
        
    while True:
        r, frame=cap.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow(windowName,gray)
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyAllWindows()

         
if __name__ ==("__main__"):
        main()
       