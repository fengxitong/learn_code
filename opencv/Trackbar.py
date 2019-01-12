# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 22:10:22 2018

@author: Administrator
"""
import numpy as np
import cv2


def nothing(x):
    pass


def draw_circle(event,x,y,flags,param):
    s=cv2.cv2.getTrackbarPos('size','image')
    b=cv2.cv2.getTrackbarPos('B','image')
    r=cv2.cv2.getTrackbarPos('G','image')
    g=cv2.cv2.getTrackbarPos('R','image')
    
    
    if event == cv2.cv2.EVENT_MOUSEMOVE:
        cv2.cv2.line(img,(x,y),(x,y),(r,g,b),s)
        
swith='0:OFF\n1:ON'
img=np.zeros((512,512,3),np.uint8)
cv2.cv2.namedWindow('image')
cv2.cv2.createTrackbar('R','image',0,255,nothing)
cv2.cv2.createTrackbar('G','image',0,255,nothing)
cv2.cv2.createTrackbar('B','image',0,255,nothing)
cv2.cv2.createTrackbar('size','image',1,255,nothing)
cv2.cv2.createTrackbar(swith,'image',0,1,nothing)
cv2.cv2.setMouseCallback('image',draw_circle)


while True:
    cv2.cv2.imshow('image',img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.cv2.destroyAllWindows()