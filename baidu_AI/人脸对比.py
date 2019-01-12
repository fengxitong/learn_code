# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 15:35:14 2018

@author: Administrator
"""
import base64 
from aip import AipFace  
import time
s=time.perf_counter()   
""" 你的 APPID AK SK """  
APP_ID = '11431643'  
API_KEY = 'gBm0U6WaN8YbSvOf0BtjiP0T'  
SECRET_KEY = 'SD28HNhvGLggASd4gGKflv0YGLoEX18y'  
  
client = AipFace(APP_ID, API_KEY, SECRET_KEY)  
  
""" 读取图片 """  
def get_file_content(filePath):  
    with open(filePath,"rb") as f:  
        # b64encode是编码，b64decode是解码  
        base64_data = base64.b64encode(f.read()) 
    image =base64_data
    return str(image,'utf-8')
#取决于image_type参数，传入BASE64字符串或URL字符串或FACE_TOKEN字符串
  
images = [  
    {'image':get_file_content('D:/12/132.jpg'),
     'image_type': 'BASE64'
    },
    {'image':get_file_content('D:/12/tu.jpg'),
     'image_type': 'BASE64'}
]  
  
""" 调用人脸比对 """  
#result_json=client.match(images);  
#print(result_json)
  
def judge(images):  
    result_json = client.match(images); #人脸对比API 
    result = result_json['result']['score']  
    if result > 90:  
        print("同一個人")  
    else:  
        print("不是同一個人")  
judge(images)
ss=time.perf_counter()
t=ss-s
print(t)