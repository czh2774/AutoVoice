#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import os
import sys
import django
import json
from lxml import etree
from django.db.models import Q
from django.forms.models import model_to_dict
sys.path.append(os.path.abspath('..'))  # 将项目路径添加到系统搜寻路径当中
os.environ['DJANGO_SETTINGS_MODULE'] = 'AutoVoice.settings'  # 设置项目的配置文件
django.setup()
import time,json,requests
from toolmodel import models
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class zuqiucaifu():
    """初始化数据
        headers：headers数据
        toy_list_dict：玩法映射表
        time_Difference:当前时间6天的差值"""
    def __init__(self):
        self.headers = {'Content-Type': 'application/json; charset=utf-8',
                   'Content-Length': '135',
                   'Host': 'appbalance.zqcf718.com',
                   'Connection': 'Keep-Alive',
                   'Accept-Encoding': 'gzip',
                   'User-Agent': 'okhttp/3.12.0'
                   }
        self.toy_list_dict = {'rq_rq3_checked': '让球胜',
                    'rq_rq1_checked': '让球平',
                    'rq_rq0_checked': '让球负',
                    'sf_sf3_checked': '胜',
                    'sf_sf1_checked': '平',
                    'sf_sf0_checked': '负',
                    'jc_yz_hjspl_checked': '亚盘主受让',
                    'jc_yz_wjspl_checked': '亚盘客受让',
                    'bd_yz_hjspl_checked': '主让',
                    'bd_yz_wjspl_checked': '客让',
                    'spf_sf3_checked': '胜',
                    'spf_sf1_checked': '平',
                    'spf_sf0_checked': '负'
                    }
        self.time_Difference=int(time.time()*1000)-6*24*60*60*1000

    """获取排行榜，进入数据库
            1、清除当前排行榜
            2、更新数据"""
    def rankings_list(self):
        db=models.zuqiumofang_user.objects
        db.all().delete()
        url='https://appbalance.zqcf718.com/vote/rankings'
        data={"params":
                  {"type":"0","v":"1","platform":"android",
                   "version_code":"8","device_type":"1",
                   "device_id":"861759031464380","version":"2.0"
                   }
              }
        value=requests.post(url=url,headers=self.headers,json=data).text
        value=json.loads(value)
        value=value['data']
        ranking=0#初始化排名数据
        for rankings_list in value:
            ranking=ranking+1
            rankings_list['ranking']=ranking
            try:
                db.get(user_id=rankings_list['user_id'])
                db.filter(user_id=rankings_list['user_id']).update(**rankings_list)
            except:

                db.create(**rankings_list)

    """获取排行榜对应的文章列表，进入数据库
        1、清除当前文章列表
        2、获取文章列表对应数据，进入数据库"""

    def userpostlist(self):
        post={}
        db=models.zuqiumofang_post.objects
        db.all().delete()
        user_db=models.zuqiumofang_user.objects
        user_id=user_db.values('user_id','ranking')
        logging.debug(user_id)
        url='https://appbalance.zqcf718.com/user/userpostlist'
        for j in user_id:
            data={"params":
                      {"page_num":"1","page_size":"10",
                       "other_user_id":j['user_id'],"exclude_ids":[],
                       "v":"1","platform":"android",
                       "version_code":"8","device_type":"1",
                       "device_id":"861759031464380","version":"2.0"
                       }
                  }
            value=requests.post(url=url,headers=self.headers,json=data).text
            value=json.loads(value)
            value=value['data']['list']
            try:
                for i in value:
                    post_id=i
                    post['post_id'] = i['label_list'][0]['post_id']
                    post['username']=i['username']
                    post['user_id']=i['user_id']
                    post['create_time']=i['create_time']
                    post['content']=i['content']
                    post['ranking']=j['ranking']
                    try:
                        db.get(post_id=post['post_id'])

                        db.filter(post_id=post['post_id']).update(**post)
                    except:

                        db.create(**post)
            except:
                pass

    """获取文章列表对应的推荐数据，并进入数据库"""
    def detail(self):
        db = models.zuqiumofang_post.objects
        post_id=db.values('post_id')
        url='https://appbalance.zqcf718.com/v4/post/detail'
        for i in post_id:
            data={"params":
                      {"post_id":i['post_id'],
                       "v":"1",
                       "platform":"android",
                       "version_code":"8",
                       "device_type":"1",
                       "device_id":"861759031464380",
                       "version":"2.0"
                       }
                  }
            value=requests.post(url=url,headers=self.headers,json=data).text
            value=json.loads(value)
            try:
                gamelist=value['data']['gameList']
            except:
                gamelist=''
            _t=db.get(post_id=i['post_id'])
            _t.strandlist=str(gamelist)
            _t.is_active=True
            _t.save()

    """生成推荐数据,并进入数据库
    1、清除当前数据
    2、获取数据，进入数据库"""
    def tuijian(self):
        post_db=models.zuqiumofang_post.objects
        user_db=models.zuqiumofang_user.objects
        tuijian_db = models.zuqiumofang_tuijian.objects
        tuijian_db.all().delete()
        logging.info(self.time_Difference)
        strandlist=post_db.values('strandlist','post_id','user_id').filter(~Q(strandlist=[]))

        for j in strandlist:
            logging.info(j)
            try:
                value=j['strandlist'].replace("'",'"')
                value=json.loads(value)
            except:
                logging.error('没有推荐数据')
                break

            for data in value:
                if 'strandList' not in data:
                    tuijian_data = {}
                    tuijian_data['post_id']=j['post_id']
                    tuijian_data['user_id']=j['user_id']
                    tuijian_data['match_id'] = data['match_id']
                    tuijian_data['home'] = data['home']
                    tuijian_data['away'] = data['away']
                    tuijian_data['ID_bet007'] = data['ID_bet007']
                    tuijian_data['create_time'] = data['create_time']
                    user_data = user_db.values('ranking', 'rc', 'wc', 'bc').filter(user_id=j['user_id'])
                    ranking = user_data[0]['ranking']
                    tuijian_data['ranking'] = int(ranking)
                    tuijian_data['rc'] = user_data[0]['rc']
                    tuijian_data['wc'] = user_data[0]['wc']
                    tuijian_data['bc'] = user_data[0]['bc']
                    tuijian_data['tuijian'] = []
                    tuijian_data['tongji']=[]
                    for i in self.toy_list_dict:
                        if i in data and data[i] == 1:
                            tuijian_data['tuijian'].append(i)
                            tuijian_data['tongji'].append(self.toy_list_dict[i])
                    try:
                        tuijian_db.get(create_time=tuijian_data['create_time'])

                        tuijian_db.filter(create_time=tuijian_data['create_time']).update(**tuijian_data)
                    except:
                        tuijian_db.create(**tuijian_data)
                else:
                    data=data['strandList']
                    for h in data:
                        data=h
                        tuijian_data = {}
                        tuijian_data['post_id'] = j['post_id']
                        tuijian_data['user_id'] = j['user_id']
                        tuijian_data['match_id'] = data['match_id']
                        tuijian_data['home'] = data['home']
                        tuijian_data['away'] = data['away']
                        tuijian_data['ID_bet007'] = data['ID_bet007']
                        tuijian_data['create_time'] = data['create_time']
                        user_data=user_db.values('ranking','rc','wc','bc').filter(user_id=j['user_id'])
                        ranking=user_data[0]['ranking']
                        tuijian_data['ranking']=int(ranking)
                        tuijian_data['rc'] = user_data[0]['rc']
                        tuijian_data['wc'] = user_data[0]['wc']
                        tuijian_data['bc'] = user_data[0]['bc']
                        tuijian_data['tuijian'] = []
                        tuijian_data['tongji'] = []
                        for g in self.toy_list_dict:
                            if g in data and data[g] == 1:
                                tuijian_data['tuijian'].append(g)
                                tuijian_data['tongji'].append(self.toy_list_dict[i])
                        try:
                            tuijian_db.get(create_time=tuijian_data['create_time'])
                            tuijian_db.filter(create_time=tuijian_data['create_time']).update(**tuijian_data)
                        except:
                            tuijian_db.create(**tuijian_data)
    """"""
    def tongji(self,match_id):
        tuijian_db=models.zuqiumofang_tuijian.objects
        betid_list=tuijian_db.values('ID_bet007','user_id','match_id','tongji','home','away','create_time','ranking','rc','wc','bc').filter(match_id=match_id)
        tuijian={}
        tuijian_list=''
        try:
            for i in betid_list:
                if int(i['create_time'])>self.time_Difference:

                    tuijian['match_id']=i['match_id']
                    tuijian['name']=i['home']+'VS'+i['away']
                    tuijian_data=str('排名'+str(i['ranking'])+'推荐'+str(i['tongji']))
                    tuijian_list=tuijian_list+' '+tuijian_data
                    print(tuijian_data)
                tuijian['tuijian_list']=tuijian_list
            tuijian=tuijian['match_id']+' '+tuijian['name']+' '+str(tuijian['tuijian_list'])
            return tuijian
        except:
            return '本场暂时没有推荐'



    def test(self):
        ob=models.zuqiumofang_post.objects
        tuijian=ob.all().exclude(strandlist=[]).__dict__

if __name__ == "__main__":
    data=zuqiucaifu()
    # data.rankings_list()
    # data.userpostlist()
    #data.detail()
    #data.tuijian()
    print(data.tongji('周二003'))
    # data.test()
