#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import os
import sys
import django
import datetime
import re
sys.path.append(os.path.abspath('..'))  # 将项目路径添加到系统搜寻路径当中
os.environ['DJANGO_SETTINGS_MODULE'] = 'AutoVoice.settings'  # 设置项目的配置文件
django.setup()
import time,json,requests
from ToolModel import models
from django.utils.timezone import now,timedelta
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
        self.time_Difference=datetime.datetime.now()-datetime.timedelta(days=3)
        self.time_doday=datetime.datetime.now()-datetime.timedelta(days=1)


    """生成昵称的方法"""
    def nickname(self):
        db=models.zuqiumofang_user.objects

        with open('nickname.txt','r',encoding='UTF-8') as f:
            iter_nickname=f.readlines()
            iter_nickname=iter(iter_nickname)

        while True:
            nickname=next(iter_nickname)
            nickname=nickname.replace('\n','')
            user_nickname=db.filter(nickname=nickname)

            if user_nickname:
                pass
            else:
                return nickname


    """将文章不统一的生成时间转化成统一的生成时间"""
    def create_time_to_date(self,create_time):


        yesterday=datetime.date.today()-datetime.timedelta(days=1)


        if '昨天' in create_time:
            create_time=yesterday.strftime('%Y-%m-%d')+' '+create_time.split()[1]+':00'
        elif '刚刚' in create_time:
            create_time=datetime.datetime.now()

        elif '分钟前' in create_time:
            minute=int(re.findall(r"\d+\.?\d*",create_time)[0])
            create_time=(datetime.datetime.now()-datetime.timedelta(minutes=minute))

        elif len(create_time)==5:
            data_time = datetime.datetime.now()
            data_time=str(data_time).split()[0]
            create_time=data_time+' '+create_time+':00'
        else:
            create_time='2019'+'-'+str(create_time)+':00'

        return create_time


    """覆盖值的方法"""
    def create_or_update(self,id,user_id,data,create_time):
        tuijian_db=models.zuqiumofang_tuijian.objects
        try:
            tuijian_db.get(id=id)
            tuijian_db.filter(id=id).update(id=id, tuijian=data, user_id=user_id,create_time=create_time)
        except:
            tuijian_db.create(id=id, tuijian=data, user_id=user_id,create_time=create_time)


    """获取排行榜，进入数据库
            1、清除当前排行榜
            2、更新数据"""
    def rankings_list(self):
        """创建数据库对象"""
        db=models.zuqiumofang_user.objects
        """请求数据，创建迭代器"""
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
        value=iter(value)#
        ranking=0#初始化排名数据
        """遍历迭代器
        如果user_id不存在，就创建，并且从未使用的nickname中获取一个最新的作为nickname，
        rankings为当前排序。
        如果user_id存在，就覆盖，rankings为当前排序"""
        for rankings_list in value:
            ranking=ranking+1
            rankings_list['ranking']=ranking
            rankings_list['nickname']=self.nickname()
            db.update_or_create(defaults=rankings_list,user_id=rankings_list['user_id'])

    """获取排行榜对应的文章列表，进入数据库
        1、清除当前文章列表
        2、获取文章列表对应数据，进入数据库"""
    def userpostlist(self):
        post={}
        db=models.zuqiumofang_post.objects
        user_db=models.zuqiumofang_user.objects
        user_id=user_db.values('user_id','ranking')
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
            value=iter(value)
            for i in value:
                if i['label_list']:
                    post['post_id'] = i['label_list'][0]['post_id']
                else:
                    post['post_id']=i['file_list'][0]['post_id']
                post['username']=i['username']
                post['user_id']=i['user_id']
                post['create_time']=self.create_time_to_date(i['create_time'])
                post['content']=i['content']
                post['ranking']=j['ranking']

                try:
                    db.get(post_id=post['post_id'])
                    db.filter(post_id=post['post_id']).update(**post)
                except:
                    db.create(**post)


    """从文章正文中获取推荐数据"""
    def tuijian_post(self):

        post_db = models.zuqiumofang_post.objects
        post_id=post_db.values('post_id').filter(create_time__gte=self.time_Difference)
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
            """判断是否有gameList并且不为空"""
            gameList=value['data']['gameList']

            if len(gameList)==1 and 'strandList' not in gameList[0] and 'home' in gameList[0]:
                for game in gameList:
                    create_time = time.localtime(game['create_time'] / 1000)
                    create_time = time.strftime("%Y-%m-%d %H:%M:%S", create_time)

                    self.create_or_update(id=game,user_id=game['user_id'],data=game,create_time=create_time)
            elif len(gameList)==1 and 'strandList' in gameList[0]:
                for game in gameList[0]['strandList']:
                    create_time = time.localtime(game['create_time'] / 1000)
                    create_time = time.strftime("%Y-%m-%d %H:%M:%S", create_time)
                    self.create_or_update(id=game,user_id=game['user_id'],data=game,create_time=create_time)
            elif len(gameList)==0:
                pass
            elif len(gameList)>1:

                for game in gameList:
                    if 'strandList' in game:
                        game=game['strandList']
                        for i in game:
                            if 'home' in i:
                                create_time = time.localtime(i['create_time'] / 1000)
                                create_time = time.strftime("%Y-%m-%d %H:%M:%S", create_time)
                                print(i)
                                self.create_or_update(id=i,user_id=i['user_id'],data=i,create_time=create_time)
                    elif 'home' in game:
                        pass

            else:

                print(gameList)


    """从文章留言中获取推荐数据"""
    def tuijian_commentlist(self):
        post_db = models.zuqiumofang_post.objects
        post_id_list = post_db.values('post_id').filter(create_time__gte=self.time_Difference)

        url = 'https://appbalance.zqcf718.com/v4/post/commentlist'
        for post_id in post_id_list:
            post_id=post_id['post_id']
            post_user_id = post_db.values('user_id').filter(post_id=post_id)
            user_id=post_user_id[0]['user_id']
            data = {
                "params":
                    {
                        "post_user_id": user_id, "page_num": "1",
                        "page_size": "10", "post_id": post_id,
                        "just_look": "1", "exclude_ids": [],
                        "v": "1", "platform": "android",
                        "version_code": "8",
                        "device_type": "1", "device_id": "861759031464380", "version": "2.0"}}
            value = requests.post(url=url, headers=self.headers, json=data).text
            value = json.loads(value)
            value = value['data']['list']

            for gamelist in value:
                if gamelist['gameList']:
                    for game in gamelist['gameList']:
                        if 'strandList'in game:
                            for i in game['strandList']:
                                create_time = time.localtime(i['create_time'] / 1000)
                                create_time = time.strftime("%Y-%m-%d %H:%M:%S", create_time)
                                self.create_or_update(id=i['id'], user_id=i['user_id'], data=i,create_time=create_time)

                        else:
                            create_time = time.localtime(game['create_time'] / 1000)
                            create_time = time.strftime("%Y-%m-%d %H:%M:%S", create_time)
                            self.create_or_update(id=game['id'],user_id=game['user_id'],data=game,create_time=create_time)


    """从user表中将推荐所需的用户数据同步到tuijian表"""
    def tuijian_data(self):
        user_db = models.zuqiumofang_user.objects
        tuijian_db = models.zuqiumofang_tuijian.objects
        tuijian_data_list=tuijian_db.values('id','user_id','tuijian')
        tuijian_data={}
        for tuijian_id in tuijian_data_list:
            user_data=user_db.get(user_id=tuijian_id['user_id'])
            tuijian=tuijian_id['tuijian'].replace("'",'"')
            tuijian_dict=json.loads(tuijian)
            tuijian_data['ranking'] = user_data.ranking
            tuijian_data['bc'] = user_data.bc
            tuijian_data['rc'] = user_data.rc
            tuijian_data['wc'] = user_data.wc
            tuijian_data['nickname']=user_data.nickname
            tuijian_data['post_id']=tuijian_dict['post_id']
            tuijian_data['ID_bet007']=tuijian_dict['ID_bet007']
            tuijian_data['away']=tuijian_dict['away']
            tuijian_data['home'] = tuijian_dict['home']
            tuijian_data['match_id'] = tuijian_dict['match_id']
            tuijian_data['state']=tuijian_dict['state']
            tuijian_data['tongji'] = []
            tuijian_list=[]
            for i in self.toy_list_dict:
                if i in tuijian_dict and tuijian_dict[i] == 1:
                    tuijian_list.append(i)
                    tuijian_data['tongji'].append(self.toy_list_dict[i])
            try:
                tuijian_db.get(id=tuijian_id['id'])
                tuijian_db.filter(id=tuijian_id['id']).update(**tuijian_data)
            except:
                tuijian_db.create(**tuijian_data)


    """根据match_id统计输出推荐"""
    def tongji(self,match_id):
        tuijian_db=models.zuqiumofang_tuijian.objects
        betid_list=tuijian_db.values('ID_bet007','user_id','match_id','tongji','home','away','create_time','ranking','rc','wc','bc','nickname').filter(match_id=match_id,create_time__gte=self.time_Difference)

        tuijian={}
        tuijian_list=''
        try:
            for i in betid_list:
                tuijian['match_id']=i['match_id']
                tuijian['name']=i['home']+'VS'+i['away']
                tuijian_data=str(i['nickname']+'推荐'+str(i['tongji']))+'\n'
                tuijian_list=tuijian_list+' '+tuijian_data
                tuijian['tuijian_list']=tuijian_list
            tuijian=tuijian['match_id']+' '+tuijian['name']+'\n'+str(tuijian['tuijian_list'])
            return tuijian
        except:
            return '本场暂时没有推荐'


    """统计当日推荐数据并输出返回"""
    def tuijian_all(self):
        tuijian_db=models.zuqiumofang_tuijian.objects
        today=datetime.datetime.now().weekday()
        weekday=['周一','周二','周三','周四','周五','周六','周日']
        weekday=weekday[today]
        #print(weekday)
        tuijian=tuijian_db.values('match_id','create_time').filter(match_id__contains=weekday,create_time__gte=self.time_doday)
        tuijian_content=[]
        for i in tuijian:


            tuijian_content.append(i['match_id'])
        #print(tuijian_content)
        set01=set(tuijian_content)
        dict01={}
        for item in set01:
            dict01.update({item:tuijian_content.count(item)})
        #print(dict01)
        value=''

        for key in dict01.keys():
            #print(key)
            data=key+'有'+str(dict01[key])+'场推荐'+'\n'
            value=value+data
        return value




if __name__ == "__main__":
    data=zuqiucaifu()


    data.rankings_list()
    # data.userpostlist()
    #data.tuijian_post()
    # data.tuijian_commentlist()
    # data.tuijian_data()
    # print(data.tongji('周六004'))
    # print(data.tuijian_all())
    # date_time=time.localtime(1559915648888/1000)

    #
    # data_time=time.strftime("%Y-%m-%d %H:%M:%S",date_time)
    # print(data_time)
    print(sys.path)