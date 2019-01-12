# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 09:36:47 2018

@author: Administrator

图片重叠
"""
import cv2 
import numpy as np
import matplotlib.pyplot as plt

img1=cv2.imread('D:\\12\\picture\\fl1.jpg')
img2=cv2.imread('D:\\12\\picture\\55.jpg')

#cv2.add(img,img1)  需要保证img img1 大小相同
# =============================================================================
# res = cv2.cv2.add(img,img1)
# cv2.cv2.imwrite('D:\\12\\tree_heart.jpg',res)
# 
# 
# cv2.imshow('image',res)
# 
# #plt.imsave('D:\\12\\blue_tree_heart.jpg',res)
# #plt.savefig('123456,jpg',res,)
# 
# cv2.imshow('image2',res)
# =============================================================================



# =============================================================================
# res=cv2.addWeighted(img1,0.6,img,0.4,1)
# 
# rows, cols, channels = img2.shape
# roi = img1[0:rows,0:cols]
# 
# img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)  #灰度
# #cv2.imshow('image',img2gray)
# 
# #binary 进行二值化    小于150为0， 150到255为255   如255改为200则大于200为显示灰度图
# #ret 为阀值（150）   mask 为二值化图像
# ret, mask = cv2.threshold(img2gray,150,255,cv2.cv2.THRESH_BINARY)
# 
# 
# 
# mask_inv= cv2.cv2.bitwise_not(mask) #获取把mask的区域取反
# 
# #mask 为掩膜 即是mask中为白色的就显示roi 黑色的显示mask的部分
# img1_bg = cv2.cv2.bitwise_and(roi,roi, mask=mask)
# cv2.imshow('image5',img1_bg)
# 
# img2_fg = cv2.cv2.bitwise_and(img2, img2, mask = mask_inv)
# cv2.imshow('image6',img2_fg)
# 
# dst = cv2.add(img1_bg, img2_fg)
# cv2.imshow('image7',dst)
# 
# img1[0:rows, 0:cols] = dst
# 
# cv2.imshow('image8',img1)
# 
# =============================================================================


# 滑条改变两张图片透明度

def nothing(x):
    pass



img = np.zeros((800,800,3),np.uint8)

cv2.namedWindow('image')

cv2.cv2.createTrackbar('a','image',0,100,nothing)

while True:
    cv2.imshow('image',img)
    
    if cv2.cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    r = cv2.cv2.getTrackbarPos('a','image')
    
    r=float(r)/100.0
    img = cv2.cv2.addWeighted(img1, r, img2, 1.0-r,0)
    cv2.cv2.imwrite('D:\\12\\picture\\fl1.jpg',img)

cv2.cv2.destroyAllWindows()
        
    


















#cv2.imwrite('D:\\12\\picture\\tree_heart_yellow2.jpg',res)















