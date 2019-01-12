# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 10:26:00 2018

@author: Administrator
"""
import requests
import itchat

KEY = 'aeea2522cf944f3c86dc131493ae62a3'


def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'dfg',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    reply = get_response(msg['Text'])
    return reply or defaultReply

itchat.auto_login(hotReload=True) 
itchat.run()











