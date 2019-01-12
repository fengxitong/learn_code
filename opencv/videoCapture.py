# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 15:57:53 2018

@author: Administrator
"""
import numpy as np
import cv2 

from aip import AipFace

cap=cv2.cv2.VideoCapture(0)


#fourcc=cv2.cv2.VideoWriter_fourcc(*'XVID')

#out=cv2.cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
APP_ID = '11406086'
API_KEY = 'ayMYdnBIf6Q5BwsDw2aTs6va'
SECRET_KEY = 'EkVpE7ao8ssPBAMGjI6ZgPxtmhdxZCeR'
        
client = AipFace(APP_ID, API_KEY, SECRET_KEY)

while cap.isOpened():
    ret, frame=cap.read()
    if ret:
       
        cv2.cv2.imwrite('D:/12/llll.JPEG',frame)
        client = AipFace(APP_ID, API_KEY, SECRET_KEY)
        #with open("D:/12/lll.JPEG","rb") as f:  
        f=open("D:/12/lll1.JPEG","rb")
        print(f)
        # b64encode是编码，b64decode是解码  
        base64_data = base64.b64encode(f.read()) 
        f.close()    
        image =base64_data
        image=str(image,'utf-8')
        
        #取决于image_type参数，传入BASE64字符串或URL字符串或FACE_TOKEN字符串
        imageType = "BASE64"
        
        """ 调用人脸检测 """
        #client.detect(image, imageType);
        
        """ 如果有可选参数 """
        options = {}
        options["face_field"] = "age"
        options["max_face_num"] = 10
        options["face_type"] = "LIVE"
        
        """ 带参数调用人脸检测 """
        
        result=client.detect(image, imageType, options)
        img = cv2.cv2.imread("D:/12/llll.JPEG")
        for i in range(result['result']['face_num']):    
            x=int(result['result']['face_list'][i]['location']['left'] )   
            h=int(result['result']['face_list'][i]['location']['height'] )   
            y=int(result['result']['face_list'][i]['location']['top']-int(h*0.5))    
            w=int(result['result']['face_list'][i]['location']['width'])   
            cv2.rectangle(img,(x,y),(x+w,y+h+int(h*0.5)//1),(0,0,255),2)    
            cv2.cv2.imshow("result",img)
                
        #frame=cv2.cv2.flip(frame,0)
        
        #out.write(frame)
        #gray = cv2.cvtColor(frame,1)
        #frame=cv2.rectangle(frame,(384,0),(510,218),(0,255,0),3)

    
#        cv2.cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) &  0xFF == ord('q'):
        break
    
    
cap.release()
#out.release()
cv2.cv2.destroyAllWindows()