#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import os
import sys
import django
sys.path.append(os.path.abspath('..'))  # 将项目路径添加到系统搜寻路径当中
os.environ['DJANGO_SETTINGS_MODULE'] = 'AutoVoice.settings'  # 设置项目的配置文件
django.setup()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
from ToolModel.tools.zuqiucaifu import zuqiucaifu
import itchat



@itchat.msg_register(itchat.content.TEXT)
def reply_msg(msg):
    try:
        if '推荐' in msg['Content']:
            print('有人请求推荐')
            itchat.send_msg("好的，稍等",msg['FromUserName'])
        elif '下载' in msg['Content']:
            print('有人请求下载！')
            f="app.jpg"
            if f:
                print('图片找到了')
            itchat.send_image(f,msg['FromUserName'])
        elif '周一' in msg['Content'] or '周二' in msg['Content'] or '周三' in msg['Content'] or '周四' in msg['Content'] or '周五' in msg['Content'] or '周六'  in msg['Content'] or '周日'  in msg['Content']:
            print('有人请求推荐',type(msg['Content']),msg['Content'])
            data=zuqiucaifu()
            data=data.tongji(match_id=msg['Content'])
            print(type(data))

            itchat.send_msg(str(data),msg['FromUserName'])
        else:
            itchat.send_msg('需要APP请发送 下载 ，需要推荐请发送请求 格式：周四004 或 周五001 这样的格式',msg['FromUserName'])
    except:
        logging.error('接受信息出错')
def it_chat_run():
    itchat.auto_login()
    itchat.run()
if __name__ == '__main__':
    it_chat_run()
