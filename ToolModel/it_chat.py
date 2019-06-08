#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import os
import sys
import django
import json
from lxml import etree
from django.db.models import Q
sys.path.append(os.path.abspath('..'))  # 将项目路径添加到系统搜寻路径当中
os.environ['DJANGO_SETTINGS_MODULE'] = 'AutoVoice.settings'  # 设置项目的配置文件
django.setup()
import time,json,requests
from ToolModel import models
from websocket import create_connection,warning
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
from google.protobuf.json_format import MessageToJson,Parse
from AutoVoice.example import addressbook_pb2
import itchat

import itchat



@itchat.msg_register(itchat.content.TEXT)
def reply_msg(msg):
    print(msg)
    if '推荐' in msg['Content']:
        print('有人请求推荐')
        itchat.send_msg("好的，稍等",msg['FromUserName'])
    elif '下载' in msg['Content']:
        print('有人请求下载！')
        itchat.send_msg('好的，给你下载地址！',msg['FromUserName'])
    else:
        itchat.send_msg('需要APP请发送 下载 ，需要推荐请发送 周四004 ',msg['FromUserName'])

if __name__ == '__main__':
    itchat.auto_login()
    time.sleep(5)
    itchat.send("文件助手你好哦", toUserName="filehelper")
    itchat.run()
