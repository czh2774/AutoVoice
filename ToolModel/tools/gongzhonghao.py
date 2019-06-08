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
import werobot

robot = werobot.WeRoBot(token='czh2774')

# @robot.handler 处理所有消息
@robot.handler
def hello(message):
    return 'Hello World!'

# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()