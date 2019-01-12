# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 15:48:12 2018

@author: Administrator
"""

import cv2
import sys
# Get user supplied values

imagePath = sys.argv[0]

cascPath = sys.argv[0]

#将图片和 cascade 名字作为命令行参数传入。我们会用 Abba 图片和 OpenCV 提供的默认 cascade 来人脸检测。

# Create the haar cascade

faceCascade = cv2.CascadeClassifier(cascPath)

#现在，我们创建一个 cascade，并用人脸 cascade 初始化。这把人脸 cascade 导入内存，所以它随时可以使用。记住，该 cascade 只是一个包含人脸检测数据的 XML 文件。

# Read the image

image = cv2.imread('D:/12/111.jpg')

#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#读取图片把它转化到灰度格式。

# Detect faces in the image

faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.cv2.CV_HAAR_SCALE_IMAGE
        )

for (x, y, w, h) in faces:

    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

#该函数返回四个值：矩形的 x 和 y 坐标，以及它的高和宽。我们用这些值和内置的 rectangle() 函数，画出矩阵。

cv2.imshow("Faces found" ,image)

cv2.waitKey(0)