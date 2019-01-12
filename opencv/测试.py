# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 17:29:31 2018

@author: Administrator
"""

import numpy 
import cv2
import matplotlib.pyplot as plt
from PIL import Image


img=numpy.loadtxt('D:\\data\\50kg\\6\\10_3.txt',skiprows=0)


#ret, img = cv2.cv2.threshold(img, , 255, cv2.cv2.THRESH_BINARY_INV)
#print(img)
#array=numpy.array([img,img,img])
## 
#array.shape=(32,32,3)
#array=abs(array-255)
#print(array)

#img=(img/numpy.max(img))*255
#img= cv2.cv2.threshold(img, 10, 255, cv2.cv2.COLOR_BGR2GRAY)

print(type(img))
#img= cv2.cv2.bitwise_not(img)

plt.imsave('D:\\12\\picture\\777.jpg',img)

img= cv2.cv2.bitwise_not(img)
#plt.subplot(231)
#plt.imshow(img,'gray')



img1=cv2.cv2.imread("D:\\12\\picture\\777.jpg")

#_,img1= cv2.cv2.threshold(img1,1, 255, cv2.cv2.THRESH_BINARY_INV)

#img1=numpy.array(img1)
print(type(img1))
#img1= cv2.cv2.bitwise_not(img1)
img2 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
#img= cv2.cv2.bitwise_not(img)
cv2.cv2.imwrite('D:\\12\\picture\\77777.jpg',img2)

#plt.subplot(232)
#plt.imshow(img)

img3=cv2.cv2.imread("D:\\12\\picture\\77777.jpg")
cv2.cv2.imshow('image',img3)

