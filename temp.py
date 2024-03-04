import cv2
import matplotlib.pyplot as plt 
def main():
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
        print(ret)
        print(frame)
    else:
        print("false")
    img1 =cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    plt.imshow(img1)
    plt.title("colour image rgb")
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
if __name__=="__main__":
    main() 