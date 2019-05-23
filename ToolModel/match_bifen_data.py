#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import socket
import os
import sys
import django


import threading
sys.path.append(os.path.abspath('..'))  # 将项目路径添加到系统搜寻路径当中
os.environ['DJANGO_SETTINGS_MODULE'] = 'AutoVoice.settings'  # 设置项目的配置文件
django.setup()
import time,json,requests
from ToolModel import models
from websocket import create_connection,warning
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
import random


class mofang_bifen():
    def bifen(self):
        url='https://live.huanhuba.com/20190521/'
        headers={'Host': 'live.huanhuba.com',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                 }


        value=requests.get(url=url,headers=headers).text
        print(value)

if __name__ == "__main__":
    data=mofang_bifen().bifen()
