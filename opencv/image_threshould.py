# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 09:40:44 2018

@author: Administrator
"""

import cv2 
import numpy as np
import matplotlib.pyplot as plt



img= cv2.cv2.imread('D:\\12\\women.jpg',0)
print(img)
ret, img1 = cv2.cv2.threshold(img, 127, 255, cv2.cv2.THRESH_BINARY)
ret, img2 = cv2.cv2.threshold(img, 127, 255, cv2.cv2.THRESH_BINARY_INV)
ret, img3 = cv2.cv2.threshold(img, 127, 255, cv2.cv2.THRESH_TRUNC)
ret, img4 = cv2.cv2.threshold(img, 127, 255, cv2.cv2.THRESH_TOZERO)
ret, img5 = cv2.cv2.threshold(img, 127, 255, cv2.cv2.THRESH_TOZERO_INV)

print(type(img2))
titles = ['original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']

images = [img, img1, img2, img3, img4, img5]

for i in range(6):   
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    
    
plt.show()



#自适应阀值
# =============================================================================
# img = cv2.cv2.medianBlur(img,5)
# 
# 
# 
# ret, th1 = cv2.cv2.threshold(img,127,255,cv2.cv2.THRESH_BINARY)
# 
# th2 = cv2.cv2.adaptiveThreshold(img, 255, cv2.cv2.ADAPTIVE_THRESH_MEAN_C,cv2.cv2.THRESH_BINARY, 11, 2)
# th3 = cv2.cv2.adaptiveThreshold(img, 255, cv2.cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.cv2.THRESH_BINARY, 11, 2)
# 
# titles = ['original Image', 'Global Threshold (v = 127)', 
#           'Adaptive Mean Thresholding', 'Adaptive Gaussian thresholding']
# 
# images = [img, th1, th2, th3]
# 
# for i in range(4):
#     plt.subplot(2, 2, i+1)
#     plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     
#     plt.xticks([]), plt.yticks([])
# plt.show()
# =============================================================================


#otsu 二值化
# =============================================================================
# ret1, th1 = cv2.threshold(img,127, 255, cv2.THRESH_BINARY)
# ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.cv2.THRESH_OTSU)
# 
# burl = cv2.cv2.GaussianBlur(img,(5,5),0)
# ret2, th3 = cv2.threshold(burl, 0, 255, cv2.THRESH_BINARY+cv2.cv2.THRESH_OTSU)
# 
# 
# cv2.imshow('image3',burl)
# cv2.imshow('image4',th3)
# 
# cv2.imshow('image',th1)
# cv2.imshow('image1',th2)
# =============================================================================


#高斯去噪公式实现（为弄懂）

# =============================================================================
# blur = cv2.GaussianBlur(img,(5,5),0)
# 
# hist = cv2.cv2.calcHist([blur],[0],None,[256],[0,256])
# print(hist)
# hist_norm = hist.ravel()/hist.max()
# 
# Q = hist_norm.cumsum()
# 
# bins = np.arange(256)
# 
# fn_min = np.inf
# 
# thresh = -1
# 
# 
# for i in range(1,256):
#     p1, p2 =np.hsplit(hist_norm,[i])
# #    print('**************************************')
# #    print(p1)
# #    print('**************************************')
# #    print(p2)
#     q1, q2 = Q[i],Q[255]-Q[i]
#     b1, b2 = np.hsplit(bins, [i])
#     
#     m1, m2 = np.sum(p1*b1)/q1,np.sum(p2*b2)/q2
#     v1, v2 = np.sum(((b1-m1)**2)*p1)/q1,np.sum(((b2-m2)**2)*p2)*q2
#     
#     fn=v1*q1+v2*q2
#     thrshv = i
#     
# ret, otsu = cv2.cv2.threshold(blur, 0, 255, cv2.cv2.THRESH_BINARY+cv2.cv2.THRESH_OTSU)
# print(ret)
# print(thresh)
# 
# cv2.imshow('image',otsu)    
# =============================================================================















