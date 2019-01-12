# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 17:55:43 2018

@author: Administrator
"""
import cv2
save_path = 'D:/12/1111.jpg'
cascade = cv2.CascadeClassifier("D:\\opencv249\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_alt_tree.xml")
cap = cv2.VideoCapture(0)
i = 0
while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    rect = cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=9,minSize=(50,50),flags = cv2.cv2.CV_HAAR_SCALE_IMAGE)
    print ("rect",rect)
    if not rect is (): 
        for x,y,z,w in rect:
            roiImg = frame[y:y+w,x:x+z]
            cv2.imwrite(save_path+str(i)+'.jpg',roiImg)
            cv2.rectangle(frame,(x,y),(x+z,y+w),(0,0,255),2)
            i +=1
    cv2.imshow('frame',frame)       
    if cv2.waitKey(1) &0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()