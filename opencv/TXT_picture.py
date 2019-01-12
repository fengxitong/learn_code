# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 08:54:58 2018

@author: Administrator
"""

import numpy 
import cv2
import matplotlib.pyplot as plt

root1='D:\\data\\50kg\\6\\10_3.txt'

root2='D:\\data\\50kg\\1\\10_3.txt'
d=[]
t=[]
with open(root1)  as f:
    dd=f.read()

    str1=str(dd)
    sp=str1.split('\n')
    for i in range(32):
        rr=sp[i].split(' ')
        for j in range(32):
            d.append(int(rr[j]))
            
        array1=numpy.array(d)
    array1=array1/2
    array1.shape=(32,32)
        
with open(root2)  as ff:
    ddd=ff.read()

    str2=str(ddd)
    sp1=str2.split('\n')
    for i in range(32):
        rrr=sp1[i].split(' ')
        for j in range(32):
            t.append(int(rrr[j]))
            
        array2=numpy.array(t)
    array2=array2/2
    array2.shape=(32,32)
        
 

img3 = cv2.cvtColor(array2,cv2.COLOR_BGR2GRAY)
_, mask= cv2.cv2.threshold(array2,80, 255,cv2.THRESH_BINARY_INV)
ret, img2 = cv2.cv2.threshold(array2, 10, 255, cv2.cv2.THRESH_BINARY_INV)           
img2= cv2.cv2.bitwise_not(mask)
img3 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
plt.imshow(array1,'gray')
plt.imshow(img2,'gray')
plt.imsave('D:\\12\\picture\\666.jpg',img2)


plt.imshow(array1,'gray')
#_, mask= cv2.cv2.threshold(array1,1, 255,cv2.THRESH_BINARY_INV)
#ret, img2 = cv2.cv2.threshold(array1, 10, 255, cv2.cv2.THRESH_BINARY_INV)           
#img3= cv2.cv2.bitwise_not(array2)
#plt.subplot(232)
#plt.imshow(img3,'gray')
#plt.imsave('D:\\12\\picture\\666.jpg',img2)
            