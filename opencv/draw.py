# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 16:43:32 2018

@author: Administrator
"""

import  numpy as np
import cv2
import matplotlib.pyplot as plt

#creat a black image
img=np.zeros((512,512,3),np.uint8)

#Draw a diagonal blue  line with thickness of 5 px
#img: figture  (0,0):左上  （511,511）;右下  （255,0,0）;RGB   5:线条粗细
img=cv2.line(img,(0,0),(511,511),(255,0,0),5)


img=cv2.rectangle(img,(384,0),(510,218),(0,255,0),3)

img=cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts=pts.reshape((-1,1,2))

img=cv2.polylines(img,[pts],True,(0,255,0),2) 

font=cv2.cv2.FONT_HERSHEY_COMPLEX  #字体
  #img  'opencv' 需要绘制的的文本 ;(10,500):字体位置（左下角） font ;1:字体大小   2：粗细
cv2.putText(img,'opencv',(10,500),font,1,(2,6,80),2,cv2.cv2.LINE_AA)


plt.imshow(img,cmap='gray')