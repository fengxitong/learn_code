# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 19:40:33 2018

@author: Administrator
"""
from aip import AipFace
import base64
import cv2

""" 你的 APPID AK SK """
APP_ID = '11406086'
API_KEY = 'ayMYdnBIf6Q5BwsDw2aTs6va'
SECRET_KEY = 'EkVpE7ao8ssPBAMGjI6ZgPxtmhdxZCeR'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)
#with open("D:/12/lll.JPEG","rb") as f:  
f=open("D:/12/lll.JPEG","rb")
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
img = cv2.cv2.imread("D:/12/lll.JPEG")
for i in range(result['result']['face_num']):    
    x=int(result['result']['face_list'][i]['location']['left'] )   
    h=int(result['result']['face_list'][i]['location']['height'] )   
    y=int(result['result']['face_list'][i]['location']['top']-int(h*0.5))    
    w=int(result['result']['face_list'][i]['location']['width'])   
    cv2.rectangle(img,(x,y),(x+w,y+h+int(h*0.5)//1),(0,0,255),2)    
    cv2.cv2.imshow("result",img)
#print(aa)
#print(aa['result']["face_num"])
#image = "取决于image_type参数，传入BASE64字符串或URL字符串或FACE_TOKEN字符串"

#imageType = "BASE64"
'''
groupId = "123456"

userId = "123456"

""" 调用人脸注册 """
client.addUser(image, imageType, groupId, userId);

""" 如果有可选参数 """
options = {}
options["user_info"] = "user's info"
options["quality_control"] = "NORMAL"
options["liveness_control"] = "LOW"

""" 带参数调用人脸注册 """
ssss=client.addUser(image, imageType, groupId, userId, options)
print(ssss)
'''