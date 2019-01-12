# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 09:13:20 2018

@author: Administrator
"""

import cv2
import numpy as np


#改变图片像素
# =============================================================================
# img=cv2.imread('D:\\12\\com11.png')
# print(img[10,10])
# for i in range(20,50):
#     for j in range(20,50):
#         img[i,j]=[0,0,0]
#         
# cv2.imshow('image',img)
#         
# =============================================================================
        
# =============================================================================
# #img=cv2.imread('D:\\12\\com.jpg')
# img=cv2.imread('D:\\12\\com11.png')
# print(img[10,10])
# sca=img.item(10,10,0)
# print(sca)   
# sca=img.itemset((10,10,0),100)
# print(sca)
# 
# =============================================================================
        
        
#图片复制 粘贴
# =============================================================================
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# 
# 
# img=cv2.imread('D:\\12\\com.jpg')
# 
# img1=cv2.imread('D:\\12\\48292.jpg')
#      #图片剪切大小应该一致
# img[150:300,100:250]=img1[0:150,0:150] #[150:300,100:250] [x:x1,y:y1]
# 
# cv2.imshow('image',img)
# cv2.imshow('image1',img1)
# 
# =============================================================================
        
    

# =============================================================================
# 
# img=cv2.imread('D:\\12\\com.jpg')
#  
# img1=cv2.imread('D:\\12\\48292.jpg')
# 
# #b, g, r = cv2.split(img1)
# g=img1[:,:,1]  #0, 1, 2, 对应 B, G, R 通道
# 
# 
# =============================================================================



'''
给图像加边框
'''

img1=cv2.imread('D:\\12\\com.jpg')
img=cv2.imread('D:\\12\\48292.jpg')

BLUE=[255,0,0]

# =============================================================================
# border 交界地区
# original  原始的
# replicate  重做
# reflect  反射
# wrap  包
# constant  不变的
# 
# =============================================================================
#original = cv2.cv2.copyMakeBorder(img,10,10,10,10,cv2.cv2.BORDER_)
replicate = cv2.cv2.copyMakeBorder(img,10,10,10,10,cv2.cv2.BORDER_REPLICATE)
reflect = cv2.cv2.copyMakeBorder(img,10,10,10,10,cv2.cv2.BORDER_REFLECT)
reflect_101 = cv2.cv2.copyMakeBorder(img,10,10,10,10,cv2.cv2.BORDER_REFLECT_101)
wrap = cv2.cv2.copyMakeBorder(img,10,10,10,10,cv2.cv2.BORDER_WRAP)
constant = cv2.cv2.copyMakeBorder(img,10,10,10,10,cv2.cv2.BORDER_CONSTANT,value=BLUE)


plt.subplot(231)
plt.imshow(img)
plt.title('replicate')

plt.subplot(232)
plt.imshow(replicate)
plt.title('replicate')

plt.subplot(233)
plt.imshow(reflect)
plt.title('reflect')

plt.subplot(234)
plt.imshow(reflect_101)
plt.title('reflect_101')

plt.subplot(235)
plt.imshow(wrap)
plt.title('wrap')

plt.subplot(236)
plt.imshow(constant)
plt.title('constant')















    
        
        
        
        