import cv2
import numpy as np
cap=cv2.VideoCapture(0)
#打开摄像头，若打开本地视频，同opencv一样，只需将０换成("×××.avi")
while(1):    # get a frame   
    ret, frame = cap.read()    # show a frame  
    cv2.imshow("capture", frame)   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("D:/12/fangjian2.jpg", frame)
        break
cap.release()
cv2.destroyAllWindows()
#释放并销毁窗口