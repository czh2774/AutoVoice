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
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

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
        ranking=0
        for i in value:
            ranking=ranking+1
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
            rankings_list['username'] = i['username']
            rankings_list['ranking']=ranking
            try:
                db.get(user_id=rankings_list['user_id'])
                #print('有这个数据')
                db.filter(user_id=rankings_list['user_id']).update(**rankings_list)
            except:
                #print('没有这个数据')
                #print(rankings_list)
                db.create(**rankings_list)


    def userpostlist(self):
        post={}
        db=models.zuqiumofang_post.objects
        user_db=models.zuqiumofang_user.objects
        user_id=user_db.values('user_id','ranking')
        print(user_id)
        url='https://appbalance.zqcf718.com/user/userpostlist'
        headers={'Content-Type': 'application/json; charset=utf-8',
                'Content-Length': '197',
                'Host': 'appbalance.zqcf718.com',
                'Connection': 'Keep-Alive',
                'Accept-Encoding': 'gzip',
                'User-Agent': 'okhttp/3.12.0'}
        for j in user_id:
            data={"params":
                      {"page_num":"1",
                       "page_size":"10",
                       "other_user_id":j['user_id'],
                       "exclude_ids":[],
                       "v":"1",
                       "platform":"android",
                       "version_code":"8",
                       "device_type":"1",
                       "device_id":"861759031464380",
                       "version":"2.0"
                       }
                  }
            value=requests.post(url=url,headers=headers,json=data)
            value=value.text
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
    def detail(self):
        db = models.zuqiumofang_post.objects
        post_id=db.values('post_id')
        url='https://appbalance.zqcf718.com/v4/post/detail'
        headers={'Content-Type': 'application/json; charset=utf-8',
                'Content-Length': '197',
                'Host': 'appbalance.zqcf718.com',
                'Connection': 'Keep-Alive',
                'Accept-Encoding': 'gzip',
                'User-Agent': 'okhttp/3.12.0'
                 }
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
            value=requests.post(url=url,headers=headers,json=data)
            value=value.text
            value=json.loads(value)
            try:
                gamelist=value['data']['gameList']
            except:
                gamelist=''
            _t=db.get(post_id=i['post_id'])
            _t.strandlist=str(gamelist)
            _t.is_active=True
            _t.save()
    def tuijian(self):
        post_db=models.zuqiumofang_post.objects
        user_db=models.zuqiumofang_user.objects
        tuijian_db = models.zuqiumofang_tuijian.objects
        toy_list = ['rq_rq3_checked',
                    'rq_rq1_checked',
                    'rq_rq0_checked',
                    'sf_sf3_checked',
                    'sf_sf1_checked',
                    'sf_sf0_checked',
                    'jc_yz_hjspl_checked',
                    'jc_yz_wjspl_checked',
                    'bd_yz_hjspl_checked',
                    'bd_yz_wjspl_checked',
                    'spf_sf1_checked',
                    'spf_sf0_checked',
                    'spf_sf3_checked'
                    ]
        strandlist=post_db.values('strandlist','post_id','user_id').filter(~Q(strandlist=[]))
        for j in strandlist:
            print(j)
            value=j['strandlist']
            value=value.replace("'",'"')
            print(value)
            value=json.loads(value)

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
                    #print(user_data)
                    ranking = user_data[0]['ranking']
                    rc = user_data[0]['rc']
                    wc = user_data[0]['wc']
                    bc = user_data[0]['bc']
                    tuijian_data['ranking'] = ranking
                    tuijian_data['rc'] = rc
                    tuijian_data['wc'] = wc
                    tuijian_data['bc'] = bc

                    tuijian_data['tuijian'] = []
                    for i in toy_list:
                        if i in data and data[i] == 1:
                            tuijian_data['tuijian'].append(i)
                    print('单场',tuijian_data)
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
                        #print(user_data)
                        ranking=user_data[0]['ranking']
                        rc=user_data[0]['rc']
                        wc=user_data[0]['wc']
                        bc=user_data[0]['bc']
                        tuijian_data['ranking']=ranking
                        tuijian_data['rc'] = rc
                        tuijian_data['wc'] = wc
                        tuijian_data['bc'] = bc

                        tuijian_data['tuijian'] = []
                        for g in toy_list:
                            if g in data and data[g] == 1:
                                tuijian_data['tuijian'].append(g)
                        #print('多选',tuijian_data)
                        try:
                            tuijian_db.get(create_time=tuijian_data['create_time'])

                            tuijian_db.filter(create_time=tuijian_data['create_time']).update(**tuijian_data)
                        except:

                            tuijian_db.create(**tuijian_data)

    def tongji(self):
        toy_list = {'rq_rq3_checked':'让球胜',
                    'rq_rq1_checked':'让球平',
                    'rq_rq0_checked':'让球负',
                    'sf_sf3_checked':'胜',
                    'sf_sf1_checked':'平',
                    'sf_sf0_checked':'负',
                    'jc_yz_hjspl_checked':'亚盘主受让',
                    'jc_yz_wjspl_checked':'亚盘客受让',
                    'bd_yz_hjspl_checked':'主让',
                    'bd_yz_wjspl_checked':'客让',
                    'spf_sf3_checked':'胜',
                    'spf_sf1_checked':'平',
                    'spf_sf0_checked':'负'
                    }
        tongji={}
        user_db=models.zuqiumofang_user.objects
        tuijian_db=models.zuqiumofang_tuijian.objects

        betid_list=tuijian_db.values('ID_bet007','user_id','match_id','tuijian','home','away','create_time','ranking','rc','wc','bc').filter(match_id='周六003')
        for i in betid_list:

            tuijian=[]
            value = i['tuijian']
            value=value.replace("'", '"')

            value = json.loads(value)
            for j in value:
                #print(j)
                tuijian.append(toy_list[j])
            print(#i['ID_bet007'],
                  i['user_id'],
                  i['match_id'],
                  i['home']+'VS'+i['away'],
                  #i['ID_bet007'],

                  #i['create_time'],
                  '排名'+str(i['ranking']),
                  '红'+str(i['rc']),
                  '走'+str(i['wc']),
                  '黑'+str(i['bc']),
                  tuijian,
                  int((int(time.time() * 1000)-int(i['create_time']))/1000/60/60),
                  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(i['create_time'])/1000))
                  )

if __name__ == "__main__":
    data=zuqiucaifu()
    #data.rankings_list()
    #data.userpostlist()
    #data.detail()
    #data.tuijian()
    data.tongji()