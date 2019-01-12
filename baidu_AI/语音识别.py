# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 16:15:07 2018

@author: Administrator
"""

from aip import  AipSpeech
import pygame 
import time
# 定义常量，此处替换为你自己的应用信息
APP_ID = '11360270'
API_KEY = 'qjS85AHq1lFrNh9bbWcrviIx'
SECRET_KEY = 'znSFDG8Ax2iGabS9XIzrRyXAjtwlHiaA '
 
# 初始化AipSpeech对象
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
 
# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
 
# 识别本地文件
#目前支持的格式较少，原始 PCM 的录音参数必须符合 8k/16k 采样率、16bit 位深、单声道，支持的格式有：pcm（不压缩）、wav（不压缩，pcm编码）、amr（压缩格式）。
result = aipSpeech.asr(get_file_content('D:/12/8k.amr'), 'amr', 8000, {'lan': 'zh'})
print (result['result'][0])
file='D:/12/8k.amr'
pygame.mixer.init()
print("播放音乐1")
track = pygame.mixer.music.load(file)
pygame.mixer.music.play()
time.sleep(6)
pygame.mixer.music.stop() 