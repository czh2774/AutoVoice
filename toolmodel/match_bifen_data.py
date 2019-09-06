#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import os
import sys
import django
from lxml import etree
sys.path.append(os.path.abspath('..'))  # 将项目路径添加到系统搜寻路径当中
os.environ['DJANGO_SETTINGS_MODULE'] = 'AutoVoice.settings'  # 设置项目的配置文件
django.setup()
import time,json,requests
from toolmodel import models
from websocket import create_connection,warning
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
from google.protobuf.json_format import MessageToJson,Parse
from AutoVoice.example import addressbook_pb2


class mofang_bifen():
    def bifen(self):
        serverid='638fb1be1e5265bb82c953a162061c6c|'+str(int(time.time()))+'|1559549450'
        url='https://app.huanhuba.com/app/score/score'
        headers={'Accept-Language': 'zh-CN,zh;q=0.8',
                'User-Agent': 'Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; kiw-al10 Build/LMY49I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Content-Length': '326',
                'Host': 'app.huanhuba.com',
                'Connection': 'Keep-Alive',
                'Accept-Encoding': 'gzip'
                 }
        cookies={'PHPSESSID':'9o557bd7a02133fucv70tn8m21',
                 'SERVERID':serverid
                 }
        data='data=%7B%22page%22%3A1%2C%22type%22%3A1%2C%22versionNum%22%3A%223.41%22%2C%22platform%22%3A%22android%22%2C%22market%22%3A%22baidu%22%2C%22android_type%22%3A0%2C%22phone_type%22%3A%22kiw-al10%22%2C%22os_version%22%3A%225.1.1%22%2C%22idfa%22%3A%22f8809957-e07f-3bcb-a7ee-80bd415274c6%22%7D&sign=eea6eb18faeec5795ac9849415d81a10'
        value=requests.post(url=url,headers=headers,cookies=cookies,data=data).text
        print(value)


        print(value)
        return value

    def huanhuba(self):
        match_data={}
        ob=models.bifen_mofang.objects
        url='https://live.huanhuba.com/20190604'
        headers={'Host': 'live.huanhuba.com',
                'Connection': 'keep-alive',
                'Cache-Control': 'max-age=0',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'If-None-Match': 'W/"54c4c-ZSDv8UFNiH/wplPKyFMNag"'
                }
        value=requests.get(url=url).text
        #print(value)
        html=etree.HTML(value)
        number=len(html.xpath('.//body/div/div/div/div/div/div/div[@data-matchid]'))
        print(number)
        for i in range(1,number+1):
            xpath=''
            xpath='.//body/div/div/div/div/div/div/div[@data-matchid]['+str(i)+']'
            match_data['match_id']=html.xpath(xpath+'/@data-matchid')
            match_data['name_league']=html.xpath(xpath+'/div/a[@title]/text()')
            match_data['time']=html.xpath(xpath+'/div[@class="td time"]/text()')
            match_data['status']=html.xpath(xpath+'/div[@class="td status"]/span/span/span[@slass="time"]/text()')
            match_data['home_name']=html.xpath(xpath+'/div[@class="td team-name home f-tar"]/a/span[@class="team-name"]/text()')
            match_data['home_ranking']=html.xpath(xpath+'/div[@class="td team-name home f-tar"]/a/span[@class="team-ranking"]/text()')
            match_data['matchhomescore']=html.xpath(xpath+'/div[@class="td vs"]/a/span[@class="win"]/span[@class="home-score"]/text()')
            match_data['away_name']=html.xpath(xpath+'/div[@class="td team-name away f-tal"]/a/span[@class="team-name f-toe"]/text()')
            match_data['away_ranking']=html.xpath(xpath+'/div[@class="td team-name away f-tal"]/a/span[@class="team-ranking"]/text()')
            match_data['matchawayscore'] = html.xpath(xpath + '/div[@class="td vs"]/a/span[@class="win"]/span[@class="away-score"]/text()')
            print(match_data)
            ob.update_or_create(**match_data)
if __name__ == "__main__":
    #print(int(time.time()))
    data=mofang_bifen().huanhuba()


