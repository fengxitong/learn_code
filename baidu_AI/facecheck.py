# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 15:43:30 2018

@author: Administrator
"""
import base64 
import cv2    
from aip import AipFace    
""" 你的 APPID AK SK """    
APP_ID = '11406086'
API_KEY = 'ayMYdnBIf6Q5BwsDw2aTs6va'
SECRET_KEY = 'EkVpE7ao8ssPBAMGjI6ZgPxtmhdxZCeR'   

imageType = "BASE64" 
""" 如果有可选参数 """    
options = {}    
options["max_face_num"] = 10 

client = AipFace(APP_ID, API_KEY, SECRET_KEY) 

cap=cv2.cv2.VideoCapture(0)

#fourcc=cv2.cv2.VideoWriter_fourcc(*'XVID')

#out=cv2.cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while True:
    ret , frame=cap.read()
    if ret:
        
        cv2.cv2.imwrite('D:/12/l66l.JPEG',frame)
        with open("D:/12/l66l.JPEG","rb") as f:  
            # b64encode是编码，b64decode是解码  
            base64_data = base64.b64encode(f.read())  
         
        #frame=cv2.cv2.flip(frame,0)
        #base64_data = base64.b64encode(frame)
        image =base64_data
        image=str(image,'utf-8') 
        result=client.detect(image,imageType , options)  
        imageType = "BASE64" 
        """ 如果有可选参数 """    
        options = {}    
        options["max_face_num"] = 10 
        print(result['result']['face_num'])    
        img=cv2.imread(r"D:/12/class.jpg")    
        for i in range(result['result']['face_num']):    
            x=int(result['result']['face_list'][i]['location']['left'] )   
            h=int(result['result']['face_list'][i]['location']['height'] )   
            y=int(result['result']['face_list'][i]['location']['top']-int(h*0.5))    
            w=int(result['result']['face_list'][i]['location']['width'])   
            cv2.rectangle(img,(x,y),(x+w,y+h+int(h*0.5)//1),(0,0,255),2)    
            cv2.imshow("result",img)    
    if cv2.waitKey(1) &  0xFF == ord('q'):
        break
   
 
# b64encode是编码，b64decode是解码  
    

cap.release()