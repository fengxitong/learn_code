# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 21:00:42 2018

@author: Administrator
"""


import cv2 
import numpy as np
import matplotlib.pyplot as plt



img= cv2.cv2.imread('D:\\12\\tree.jpg',0)
#cv2.imshow('image',img)

# =============================================================================
# #放大
# #img 图像  None当为图像尺寸时  fx x轴放大倍数 fy y轴放大倍数  interpolation 放大运算方式  
# #包含cv2.INTER_AREA   cv2.INTER_CUBIC(慢)  cv2.INTER_LINEAR(为默认)
# res1 = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.cv2.INTER_CUBIC)
# cv2.imshow('image2',res1)
# 
# =============================================================================




# =============================================================================
# height, width=img.shape[:2]
# 
# res = cv2.resize(img, (2*width, 2*height), interpolation = cv2.INTER_CUBIC)
# 
# cv2.imshow('image1',res)
# =============================================================================

#移动
# =============================================================================
# rows, cols=img.shape
# 
# M = np.float32([[1,0,100],[0,1,50]])
# 
# dst = cv2.warpAffine(img,M,(cols,rows))
# 
# cv2.imshow('img',dst)
# =============================================================================


#旋转
# =============================================================================
# rows, cols= img.shape
# 
# M = cv2.cv2.getRotationMatrix2D((cols/2, rows/2),90,1)
# 
# dst = cv2.cv2.warpAffine(img, M, (cols, rows))
# 
# cv2.imshow('image3',dst)
# =============================================================================







