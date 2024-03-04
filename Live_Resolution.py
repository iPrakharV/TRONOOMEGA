import cv2

def main():
    windowName="Live Feed"
    cv2.namedWindow("Live Feed")
    
    cap = cv2.VideoCapture(0)
    print('width:'+str(cap.get(3)))
    print('width:'+str(cap.get(4)))
    
    cap.set(3,256)
    cap.set(4,192)
    
    print('width:'+str(cap.get(3)))
    print('width:'+str(cap.get(4)))
    
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
       