import cv2

def main():
    windowName="Live Feed"
    cv2.namedWindow("Live Feed")
    
    cap = cv2.VideoCapture(0)
    cam = cv2.VideoCapture(1)
    rec = cv2.VideoCapture(2)
    print('width:'+str(cap.get(3)))
    print('height:'+str(cap.get(4)))
    
    cap.set(3,384)
    cap.set(4,288)
    cam.set(3,384)
    cam.set(4,288)
    rec.set(3,384)
    rec.set(4,288)
    
    print('width:'+str(cap.get(3)))
    print('height:'+str(cap.get(4)))
    
    while True:
        ret, frame=cap.read()
        tre, slide=cam.read()
        rte, shot=rec.read()
        cv2.imshow(windowName,frame)
        cv2.imshow("feed2",slide)
        cv2.imshow("feed3",shot)
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyAllWindows()

         
if __name__ ==("__main__"):
        main()
       