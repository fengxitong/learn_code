# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 20:24:20 2018

@author: Administrator
"""

import numpy as np
import cv2 


'''
color tranfroms


'''

#获取color attribute
#flags=[i for i in dir(cv2) if i.startswith('COLOR_')]
#print(flags)


# =============================================================================
# cap=cv2.cv2.VideoCapture(0)
# 
# 
# while True:
#     ret, frame=cap.read()
#     hsv = cv2.cv2.cvtColor(frame,cv2.cv2.COLOR_BGR2HSV)
#     
#     lower_blue = np.array([110,50,50])  #设定蓝色阀值
#     upper_blue = np.array([130,255,255])
#     
#     
#     #cv2.inRange(图片（矩阵），阀值下限，阀值上限 ) 输出和输入相同的矩阵对于通道的处理
#     mask = cv2.cv2.inRange(hsv,lower_blue,upper_blue)
#     res = cv2.cv2.bitwise_and(frame,frame,mask=mask) #对源图像处理
#     
#     cv2.imshow('frame',frame)
#     cv2.imshow('mask',mask)
#     cv2.imshow('res',res)
#     
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# 
# cap.release()
# cv2.destroyAllWindows()
# =============================================================================


# =============================================================================
# green = np.uint8([[[0,255,0]]])
# 
# hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
# 
# print(hsv_green)
# =============================================================================




img= cv2.imread('D:\\12\\red_blue_green.jpg')

hsv = cv2.cv2.cvtColor(img,cv2.cv2.COLOR_BGR2HSV)


lower_blue = np.array([110,100,100])#blue
upper_blue = np.array([130,255,255])

lower_green = np.array([60,100,100]) #green
upper_green = np.array([70,255,255])

lower_red = np.array([0,100,100])  #red
upper_red = np.array([10,255,255])

red_mask = cv2.inRange(hsv,lower_red,upper_red,)  #red
blue_mask = cv2.inRange(hsv,lower_blue,upper_blue)#blue
green_mask = cv2.inRange(hsv, lower_green, upper_green)  #green

red = cv2.bitwise_and(img,img,mask=red_mask)
blue = cv2.bitwise_and(img,img,mask=blue_mask)
green = cv2.bitwise_and(img,img,mask=green_mask)

res = red + blue +green

#cv2.imshow('img',img)
#cv2.imshow('res',res)


'''
将图变白然后将取出的red或者其他颜色与之相加
'''
# =============================================================================
# white_lower = np.array([0,0,0])
# white_upper = np.array([1,1,1])
# 
# img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('img2',img2)
# ret, white = cv2.threshold(img2,0,255,cv2.cv2.THRESH_BINARY)
# 
# cv2.imshow('image',white)
# #white  = cv2.bitwise_and(img,img,mask= white_mask)
# white1 = cv2.cvtColor(white,cv2.cv2.COLOR_GRAY2BGR)
# wr=red+white1+green+blue
# cv2.imshow('white',wr)
# #cv2.destroyAllWindows()
# =============================================================================





