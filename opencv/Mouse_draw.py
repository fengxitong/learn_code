# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 20:11:05 2018

@author: Administrator
"""

import numpy as np
import cv2


# =============================================================================
# x1,y1 = 1,1  #x1, y1 需要定义成全局变量，否者会在不同elif中作用域不同， 导致无法调用
# 
# def draw_circle(event,x,y,flags,param):
#     global x1, y1
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         cv2.cv2.circle(img,(x,y),50,(255,80,90),1)#鼠标左键双击画圆
#         
#     elif event == cv2.cv2.EVENT_MOUSEMOVE:
#         cv2.cv2.line(img,(x,y),(x,y),(255,0,0),2)
#     
#     elif event == cv2.cv2.EVENT_LBUTTONDOWN:
#         x1, y1 =x, y     #为矩形左上点赋值
#         
#     elif event == cv2.cv2.EVENT_LBUTTONUP:
#         cv2.cv2.rectangle(img,(x1,y1),(x,y),(0,255,0),3) #选定区域画矩形
#     
# img=np.zeros((512,512,3),np.uint8)
# 
# cv2.namedWindow('image')
# 
# cv2.setMouseCallback('image',draw_circle)
# 
# while True:
#     cv2.imshow('image',img)
#     
#     if cv2.waitKey(20) & 0xFF == ord('q'): 
#         break
#     
#     
# cv2.cv2.destroyAllWindows()
# =============================================================================

drawing = False
ix, iy= -1,-1
px,py=-1, -1


def draw_circle(event,x,y,flags,param):
    global ix, iy, px, py, drawing
    
    if event == cv2.cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy=x,y
    elif event == cv2.cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if px == -1:
                cv2.cv2.rectangle(img,(ix,iy),(px,py),(0,0,0),0) #将前一帧的矩形涂黑
            else:
                cv2.cv2.rectangle(img,(ix,iy),(px,py),(80,0,0),0)
            cv2.cv2.rectangle(img,(ix,iy),(x,y),(80,0,0),0)
            px, py=x, y
    elif event == cv2.cv2.EVENT_LBUTTONUP:
        drawing= False
        cv2.cv2.rectangle(img,(ix,iy),(x,y),(80,0,0),0)
        px, py=-1, -1

img=np.zeros((512,512,3),np.uint8)
 
cv2.namedWindow('image')
 
cv2.setMouseCallback('image',draw_circle)
 
while True:
    cv2.imshow('image',img)
     
    if cv2.waitKey(20) & 0xFF == ord('q'): 
        break
     
     
cv2.cv2.destroyAllWindows()