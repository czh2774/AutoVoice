#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import socket
import os
import sys
import django

import websocket
import threading
sys.path.append(os.path.abspath('..'))  # 将项目路径添加到系统搜寻路径当中
os.environ['DJANGO_SETTINGS_MODULE'] = 'AutoVoice.settings'  # 设置项目的配置文件
django.setup()
import time,json,requests
from toolmodel import models
import requests,re
import toolmodel.tools.ym
import toolmodel.tools.chaojiying

import json

from django.http import HttpResponse





#mobile = toolmodel.tools.ym.ym_data().get_mobile()
class vipc_data():
    def __init__(self):
        self.mobile=toolmodel.tools.ym.ym_data().get_mobile()
    def get_image_url(self):
        url='https://passport.vipc.cn/api/v2/verification/message/register'
        headers={'Content-Type': 'application/json; charset=UTF-8',
                 'Host':'passport.vipc.cn',
                 'Connection': 'Keep-Alive',
                 'Accept-Encoding': 'gzip',
                 'User-Agent': 'gzip'}
        data={"mobile":self.mobile,
                "password":"1234567z",
                "messageCode":"",
                "imageVerifyCode":"",
                "appId":"vipc",
                "fr":"officer",
                "pf":"android"}
        data=json.dumps(data)#转换格式
        cookies={'vid':'5cab1532aab2b40023d61752',
                 'imei':'865166028801226',
                 'app':'vipc-android',
                 'chnl':'officer',
                 'ver':'5.6.4'}
        respones=requests.post(url=url,headers=headers,cookies=cookies,data=data)

        respones=respones.text
        url=json.loads(respones)

        url=url['imageVerifyUri']

        print('<<<<<<图形验证码识别地址', url)
        return url
    # def get_image(self):
    #     print('正在请求唯彩会图形验证码>>>>>>>')
    #     url=self.get_image_url()
    #     headers={'Host': 'passport.vipc.cn',
    #     'Connection': 'Keep-Alive',
    #     'Accept-Encoding': 'gzip',
    #     'User-Agent': 'gzip'}
    #     cookies = {'vid': '5cab1532aab2b40023d61752',
    #                'imei': '865166028801226',
    #                'app': 'vipc-android',
    #                'chnl': 'officer',
    #                'ver': '5.6.4'}
    #     respones=requests.get(url=url,headers=headers,cookies=cookies)
    #
    #     with open('a.jpg','wb') as f:
    #         f.write(respones.content)
    #     value=static.chaojiying.Chaojiying_Client('czh2774', 'Zhangquan1', '899066').PostPic(open('a.jpg', 'rb').read(),1004)
    #
    #     value=value['pic_str']
    #     print('<<<<<<图形验证码识别结果',value)
    #     return value
    def get_register(self):

        #imageVerifyCode=self.get_image()
        url='https://passport.vipc.cn/api/v2/verification/message/register'

        headers = {'Host': 'passport.vipc.cn',
                   'Connection': 'Keep-Alive',
                   'Content-Length':'132',
                   'Accept-Encoding': 'gzip',
                   'User-Agent': 'gzip'}
        cookies = {'vid': '5cab1532aab2b40023d61752',
                   'imei': '865166028801226',
                   'app': 'vipc-android',
                   'chnl': 'officer',
                   'ver': '5.6.4'}
        data = {"mobile": self.mobile,
                "password": "1234567z",
                "messageCode": "",
                "imageVerifyCode": "",
                "appId": "vipc",
                "fr": "officer",
                "pf": "android"}
        #data=json.dumps(data)
        response=requests.post(url=url,cookies=cookies,headers=headers,data=data)
        response=response.text
        print('<<<<<<验证码输入结果',response)
        return response
    def user_reqister(self):
        ok=self.get_register()
        #ok='1'
        messageCode=toolmodel.tools.ym.ym_data().get_release(mobile=self.mobile)
        messageCode=re.sub("\D", "", messageCode)

        print('手机验证码：',messageCode)
        if ok:
            url='https://passport.vipc.cn/api/v2/auth/register'
            headers = {'Host': 'passport.vipc.cn',
                       'Content - Type': 'application / json;charset = UTF - 8',
                       'Connection': 'Keep-Alive',
                       'Content-Length': '112',
                       'Accept-Encoding': 'gzip',
                       'User-Agent': 'gzip'}
            cookies = {'vid': '5cab1532aab2b40023d61752',
                       'imei': '865166028801226',
                       'app': 'vipc-android',
                       'chnl': 'officer',
                       'ver': '5.6.4'}
            data = {"mobile": self.mobile,
                    "password": "1234567z",
                    "messageCode": messageCode,
                    "appId": "vipc",
                    "fr": "officer",
                    "pf": "android"}
            response=requests.post(url=url,headers=headers,cookies=cookies,data=data)
            response=response.text
            print('<<<<<<注册账号数据',response)
            with open(r'vipc.txt',"a",encoding="utf-8") as f:
                f.write(str(response))
                f.write('\n')

            response=json.loads(response)
            value={}
            value['mobile'] = response['mobile']
            value['password'] = '1234567z'
            value['isdead'] = '0'
            value['utk'] = response['utk']
            value['token'] = response['token']
            value['user_id'] = response['_id']
            value['nutk'] = response['nutk']
            return value

if __name__ == '__main__':
    for i in range(1,11):
        #mobile = ym.ym_data().get_mobile()
        data=vipc_data()
        #data.get_image_url()
        #data.match_fx()
        #print(data.get_image())
        #print(data.get_register())

        print(data.user_reqister())
        #time.sleep(120)


























#print(type(data))
#print(data)
#print(data.match_fx())