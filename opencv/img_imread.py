# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 10:51:05 2018

@author: Administrator
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('D:\\12\\com.jpg',-1)   #读取图片 -1 alpha通道
img1=cv2.imread('D:\\12\\class.jpg',1)  #1是 RGB通道   0 是灰度读取


#cv2.imshow('image',img)
#cv2.imshow('Image1',img1)   #显示图片

plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.xticks([])  #隐藏 x,y 轴上的刻度值
plt.yticks([])  

plt.show()

k=cv2.waitKey(0) #等待键盘输入
if k==ord('s'):
    cv2.cv2.imwrite('save.jpg',img1)   #读入图片

elif k==27:
    cv2.cv2.destroyAllWindows()  #关闭窗口
    
