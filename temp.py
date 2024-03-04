import cv2
def main():
    cap1 = cv2.VideoCapture(0)
    cap1.set(3,384)
    cap1.set(4,288)
    cap2 = cv2.VideoCapture(1)
    cap2.set(3,384)
    cap2.set(4,288)
    cap3 = cv2.VideoCapture(2)
    cap3.set(3,384)
    cap3.set(4,288)
    if cap1.isOpened():
        r, frame1 = cap1.read()
        e, frame2 = cap2.read()
        t, frame3 = cap3.read()
    else:
        print("false")
    cv2.imshow("cam1",frame1)
    cv2.imshow("cam2",frame2)
    cv2.imshow("cam3",frame3)
    
if __name__=="__main__":
    main() 