# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 17:12:54 2018

@author: Administrator
"""

import cv2
import sys
import importlib
importlib.reload(sys)
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(1, 10.0)
#此处fourcc的在MAC上有效，如果视频保存为空，那么可以改一下这个参数试试, 也可以是-1
#fourcc = cv2.cv2.CVCV_FOURCC('m', 'p', '4', 'v')
# 第三个参数则是镜头快慢的，10为正常，小于10为慢镜头
out = cv2.VideoWriter('D:/12/output2.avi', -1,10,(640,480))
#-1 程序运行时弹出选择视频编码格式
while True:
    ret,frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 1)
        a = out.write(frame)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()