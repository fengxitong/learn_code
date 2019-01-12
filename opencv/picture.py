# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 11:21:57 2018

@author: Administrator
"""

import numpy 
import cv2
import os
import matplotlib.pyplot as plt
from PIL import Image

def picture(root,savedir,true_root):
    '''
        将txt数据文档转化为灰度图片
        其中由于技术能力问题，导致无法直接转化（没有找到直接存储为灰度图片的方法）
        中间利用电脑自身的存储机制将图片转彩色，然后重新读取后转灰色，保存为灰度图片
        opencv保存和matplotlib 保存效果不一致
    
    
    '''
    img=numpy.loadtxt(root,skiprows=0)  #读取存为txt文档的数据
    img= cv2.cv2.bitwise_not(img)  #二值化
    plt.imsave(savedir,img)  #临时存放
    img=cv2.cv2.imread(savedir)  #重新读取
    img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #灰度转换
    cv2.cv2.imwrite(true_root,img1)   #最终保存
    
root='D:\\data\\kkk'
    
def dir_itmes(root):
    for root, dirs, files in os.walk(root):
        for i, file in enumerate(files):
            file2='\\'+str(i)+'.jpg'
            str1=root.replace('data','picture')
            #str1=str1.replace('\\','\\\\')
            if not os.path.exists(str1):
                os.makedirs(str1)
            
            str2=str1+file2
            picture(os.path.join(root,file),'D:\\12\\picture\\123456.jpg',str2)
            
        for dir in dirs:
            dir_itmes(dir)
            
            
            
# =============================================================================
# def bianli(root):
#     for root, dirs, files in os.walk(root):
#         for i, file in enumerate(files):
#             
#             file1=os.path.splitext(file)
#             file2='\\'+str(i)+'.jpg'
#             print(os.path.join(root,file))
#             str1=os.path.join(root,file)
#             print(root.replace('data','picture')+file2)
#         for dir in dirs:
#             bianli(dir)
# =============================================================================
    
dir_itmes(root)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    