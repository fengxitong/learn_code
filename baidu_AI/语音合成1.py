# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 18:50:44 2018

@author: Administrator
"""

from aip import  AipSpeech
import time
import pygame 
# 定义常量，此处替换为你自己的应用信息
APP_ID = '11392469'
API_KEY = 'F8Dv2t4Dn3jF3OtLISMtxzea'
SECRET_KEY = 'GNYRGXKKLnDpeR3AN67baKG7FkhRs9Yo'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result  = client.synthesis('你好 欢迎来到PLC实验室 您是否进入', 'zh', 1, {
    'vol': 5,})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('D:/12/auido0.mp3','wb') as f:
        f.write(result)
        

file='D:/12/auido0.mp3'
pygame.mixer.init()
print("播放音乐1")
track = pygame.mixer.music.load(file)
pygame.mixer.music.play()
time.sleep(3)
pygame.mixer.music.stop()        
