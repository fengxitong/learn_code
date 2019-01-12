# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 10:36:28 2019

@author: Administrator
"""

# =============================================================================
# import cv2
# import numpy as np
# 
# img = cv2.imread('E:/12/women.jpg' ,0)
# 
# ret, thresh = cv2.threshold(img, 127, 255,0)
# 
# img,contours,hierarchy = cv2.findContours(thresh, 1, 2)
# 
# cnt = contours[0]
# M = cv2.moments(cnt)
# print(M)
# =============================================================================


import cv2
import numpy as np

img = cv2.imread('E:/12/women.jpg' ,0)
ret,thresh = cv2.threshold(img,127,255,0)
img,contours,hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[1]
hull = cv2.convexHull(cnt,returnPoints=False)

print(hull)

k = cv2.isContourConvex(cnt)


x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img,[box],0,(0,0,255),2)














