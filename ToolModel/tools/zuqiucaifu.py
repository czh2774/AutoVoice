#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import os
import sys
import django
import json
from lxml import etree
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

class zuqiucaifu():
    def rankings_list(self):
        rankings_list={}
        db=models.zuqiumofang_user.objects
        url='https://appbalance.zqcf718.com/vote/rankings'
        headers={'Content-Type': 'application/json; charset=utf-8',
                'Content-Length': '135',
                'Host': 'appbalance.zqcf718.com',
                'Connection': 'Keep-Alive',
                'Accept-Encoding': 'gzip',
                'User-Agent': 'okhttp/3.12.0'
                }
        data={"params":
                  {"type":"0",
                   "v":"1",
                   "platform":"android",
                   "version_code":"8",
                   "device_type":"1",
                   "device_id":"861759031464380",
                   "version":"2.0"}}
        value=requests.post(url=url,headers=headers,json=data)
        value=value.text
        value=json.loads(value)
        value=value['data']
        for i in value:
            print(i)
            rankings_list['user_id']=i['user_id']
            rankings_list['has_game']=i['has_game']
            rankings_list['is_author']=i['is_author']
            rankings_list['is_follow']=i['is_follow']
            rankings_list['poster']=i['poster']
            rankings_list['rc']=i['rc']
            rankings_list['wc']=i['wc']
            rankings_list['bc']=i['bc']
            rankings_list['rr']=i['rr']
            rankings_list['sr']=i['sr']
            rankings_list['vote_number']=i['vote_number']
            db.update_or_create(**rankings_list)
        print(value)

if __name__ == "__main__":
    data=zuqiucaifu()
    data.rankings_list()