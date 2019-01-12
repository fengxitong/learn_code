# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 22:19:09 2018

@author: Administrator
"""


import cv2 
import numpy as np
import matplotlib.pyplot as plt



img= cv2.cv2.imread('D:\\12\\tree.jpg',0)


kernel = np.ones((5,5), np.float32)/25

dst = cv2.filter2D(img, -1, kernel)


cv2.imshow('image1',img)

#plt.subplot(232)
cv2.imshow('image2',dst)
