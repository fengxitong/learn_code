# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 15:57:20 2018

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

result = client.match([
    {
        'image': str(base64.b64encode(open('D:/12/132.jpg', 'rb').read())),
        'image_type': 'BASE64'
    },
    {
        'image': str(base64.b64encode(open('D:/12/tu.jpg', 'rb').read())),
        'image_type': 'BASE64'
    }
])
ss=time.perf_counter()
t=ss-s
print(result)
print(t)