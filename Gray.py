import cv2

def main():
    windowName="Live Feed"
    cv2.namedWindow("Live Feed")
    
    cap = cv2.VideoCapture(0)
    cap.set(3,300)
    cap.set(4,200)
    
    
    if cap.isOpened():
        ret, frame = cap.read()
        print(ret)
        print(frame)
    else:
        ret=False
        
    while ret:
        ret, frame=cap.read()
        cv2.imshow(windowName,frame)
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyAllWindows()

         
if __name__ ==("__main__"):
        main()
       