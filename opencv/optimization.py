# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 20:12:39 2018

@author: Administrator
"""

import numpy as np
import cv2



#opencv 默认优化
e1=cv2.cv2.getTickCount()

s=1+1

e2=cv2.getTickCount()

time=(e2-e1)/cv2.getTickFrequency()
print(time)
print(cv2.cv2.useOptimized())


#关闭优化
cv2.cv2.setUseOptimized(False)
e1=cv2.cv2.getTickCount()

s=1+1

e2=cv2.getTickCount()

time=(e2-e1)/cv2.getTickFrequency()
print(time)
print(cv2.cv2.useOptimized())




