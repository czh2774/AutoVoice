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
from websocket import create_connection,warning
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
import random


class hiyuncai():
    def __init__(self):
        self.cookie={'__cfduid':'d2fea3366a40c8fc6009657f4c1e297301558604732',
                     'Hm_lvt_ca444009ad5fa2879a3b88d9ccf4b2a4':'1556420393',
                     'Hm_lvt_8189975adf5a41c4bcd46ea137aed48c':'1556544330,1556723397,1557532449,1557736563',
                     'Hm_lpvt_8189975adf5a41c4bcd46ea137aed48c':'1557737068'
                     }
    def login_do(self):
        url='https://jw-api.myspgame.com/user/login.do'
        header={'Host': 'jw-api.myspgame.com',
                'Connection': 'keep-alive',
                'Content-Length': '85',
                'Accept': 'application/json, text/plain, */*',
                'Origin': 'http://www.hiyuncai.vip',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Referer': 'http://www.hiyuncai.vip/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9'
                }
        cookies={'JSESSIONID':'7ca34651-aa9d-4746-9dcd-5b7f40883c4b'}
        data={'userName':'admin54478',
              'passWord':'af09f4d4cc896f1ceb2496105185401b',
              'domain':'www.hiyuncai.vip'
              }
        value=requests.post(url=url,
                            headers=header,
                            cookies=cookies,
                            data=data)
        value=value.cookies
        print(value)
    def waitForTicket(self):
        url='http://www.hiyuncai.vip/view/lottery/waitForTicket.html?t=6a20dc9309b999ea0dfa25be86b3eec3'
        header={'Host': 'www.hiyuncai.vip',
                'Proxy-Connection': 'keep-alive',
                'Pragma': 'no-cache',
                'Accept': 'text/html',
                'Cache-Control': 'no-cache',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
                'Referer': 'http://www.hiyuncai.vip/',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9'
                }

        value=requests.get(headers=header,
                           url=url,

                           cookies=self.cookie
                           )
        value.encoding='utf-8'
        value=value.text
        print(value)
    def pending_options(self):
        url='https://jw-api.myspgame.com/ticket/pending.do'
        header={'Host': 'jw-api.myspgame.com',
                'Connection': 'keep-alive',
                'Access-Control-Request-Method': 'POST',
                'Origin': 'http://www.hiyuncai.vip',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
                'Access-Control-Request-Headers': 'x-requested-with',
                'Accept': '*/*',
                'Referer': 'http://www.hiyuncai.vip/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9'
                }
        value=requests.options(url=url)
        value=value.text
        print(value)

    def pending_post(self):
        url='https://jw-api.myspgame.com/ticket/pending.do'
        header={'Host': 'jw-api.myspgame.com',
                'Connection': 'keep-alive',
                'Content-Length': '85',
                'Accept': 'application/json, text/plain, */*',
                'Origin': 'http://www.hiyuncai.vip',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Referer': 'http://www.hiyuncai.vip/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',

                }
        cookie={'JSESSIONID':'7ca34651-aa9d-4746-9dcd-5b7f40883c4b'}
        # data='pageNo=1&pageSize=60&dateSort=&priceSort=&userName=&ticketId=&domain=www.hiyuncai.vip'
        data={'pageNo':'1',
            'pageSize':'60',
            'dateSort':'',
            'priceSort':'',
            'userName':'',
            'ticketId':'',
            'domain':'www.hiyuncai.vip'}
        value=requests.post(headers=header,
                           url=url,
                           cookies=cookie,
                           data=data
                           )

        value=value.text
        print(value)
        value=json.loads(value)
        betId_list=[]
        for i in value['data']['pageList']:
            print(i['betId'])
            betId=i['betId']
            betId_list.append(betId)
        return betId_list

    def orderid_post(self):
        url='https://jw-api.myspgame.com/order/wait.do'
        header={'Host': 'jw-api.myspgame.com',
                'Connection': 'keep-alive',
                'Accept': 'application/json,text/plain, */*',
                'Origin': 'http://www.hiyuncai.vip',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Referer': 'http://www.hiyuncai.vip/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9'
                }
        cookie={'JSESSIONID':'7ca34651-aa9d-4746-9dcd-5b7f40883c4b'}
        ticketId_list=self.pending_post()
        id_list=[]

        for i in ticketId_list:
            data = {'pageNo': '1',
                    'pageSize': '30',
                    'ticketId': i}
            value=requests.post(url=url,headers=header,cookies=cookie,data=data)
            value=value.text
            value=json.loads(value)

            #print(value)
            betId_orders = {}
            betId_orders['applyid'] = []
            for j in value['data']['orders']['pageList']:
                betId_orders['betId']=value['data']['betId']

                betId_orders['applyid'].append(j['applyid'])
                print(betId_orders)
            id_list.append(betId_orders)
            print(id_list)
        return id_list

    def handle_post(self):
        url='https://jw-api.myspgame.com/order/handle.do'
        url1='https://jw-api.myspgame.com/ticket/handle.do'
        headers={'Host': 'jw-api.myspgame.com',
                'Connection': 'keep-alive',
                'Accept': 'application/json, text/plain, */*',
                'Origin': 'http://www.hiyuncai.vip',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Referer': 'http://www.hiyuncai.vip/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9'
                }
        cookie = {'JSESSIONID': '7ca34651-aa9d-4746-9dcd-5b7f40883c4b'}
        id_list=self.orderid_post()
        for i in id_list:
            data={'orderIds':i['applyid'],
                 'orderStatus':'3',
                  'ticketId':i['betId']
                  }
            value=requests.post(url=url,data=data,cookies=cookie,headers=headers)
            print(value.text)
            data1 = {'equipment': '',
                     'equipmentCode': '',
                     'equipmentType': '3',
                     'ticketIds': i['betId'],
                     'ticketStatus': '3'}
            value1=requests.post(url=url1,data=data1,cookies=cookie,headers=headers)
            print(value1.text)
            time.sleep(15)

    def wait_post(self):
        url='https://jw-api.myspgame.com/order/wait.do'
        url1='https://jw-api.myspgame.com/ticket/handle.do'
        headers={'Host': 'jw-api.myspgame.com',
                'Connection': 'keep-alive',

                'Accept': 'application/json, text/plain, */*',
                'Origin': 'http://www.hiyuncai.vip',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Referer': 'http://www.hiyuncai.vip/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9'
                }
        cookies={'JSESSIONID':'7ca34651-aa9d-4746-9dcd-5b7f40883c4b'}
        data={'pageNo':'1',
              'pageSize':'30',
              'ticketId':'257464208'
              }
        data1={'equipment':'',
              'equipmentCode':'',
               'equipmentType':'3',
              'ticketIds':'257441689',
               'ticketStatus':'3'}
        # value=requests.post(url=url,
        #                     headers=headers,
        #                     cookies=cookies,
        #                     data=data)
        # value=value.text
        # print(value)
        value1=requests.post(url=url1,
                             headers=headers,
                             cookies=cookies,
                             data=data1)
        value1=value1.text
        print(value1)
if __name__ == "__main__":
    data=hiyuncai()
    #data.login_do()
    #data.waitForTicket()
    #data.pending_options()
    #data.pending_post()
    #data.orderid_post()


    while True:
        data.handle_post()
        time.sleep(60)
    #data.wait_post()
