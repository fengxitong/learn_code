# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 09:47:27 2019

@author: Administrator
"""

# =============================================================================
# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
# img=cv2.cv2.imread('E:/12/women.jpg', 0)
# 
# laplacian=cv2.cv2.Laplacian(img,cv2.CV_64F) #CV_64F为图像深度
# 
# sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)#1，0参数表示在x方向求一阶导数
# 
# sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)#0,1参数表示在y方向求一阶导数
# 
# plt.subplot(2,2,1), plt.imshow(img,cmap = 'gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,2), plt.imshow(laplacian,cmap = 'gray')
# plt.title('Laplacian'),  plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,3), plt.imshow(sobelx,cmap = 'gray')
# plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,4), plt.imshow(sobely,cmap = 'gray')
# plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
# plt.show()
# =============================================================================



# =============================================================================
# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
# 
# img = cv2.imread('E:/12/women.jpg',0)
# 
# edges = cv2.Canny(img,100,200)
# 
# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image')
# 
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image')
# plt.show()
# =============================================================================






import cv2
import numpy as np
from matplotlib import pyplot as plt

def nothing(x):
    pass

cv2.namedWindow('res')

cv2.createTrackbar('max','res',0,255,nothing)
cv2.createTrackbar('min','res',0,255,nothing)

img = cv2.imread('E:/12/women.jpg',0)

maxVal=200
minVal=100

while (1):

    if cv2.waitKey(20) & 0xFF==27:
        break
    maxVal = cv2.getTrackbarPos('min','res')
    minVal = cv2.getTrackbarPos('max','res')
    if minVal < maxVal:
        edge = cv2.Canny(img,100,200)
        cv2.imshow('res',edge)
    else:
        edge = cv2.Canny(img,minVal,maxVal)
        cv2.imshow('res',edge)
cv2.destoryAllWindows()
















