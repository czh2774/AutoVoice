import sys
import os
import django
import logging
import time

sys.path.append(os.path.abspath('..'))  # 将项目路径添加到系统搜寻路径当中
os.environ['DJANGO_SETTINGS_MODULE'] = 'AutoVoice.settings'  # 设置项目的配置文件
django.setup()
import time, json, requests
from toolmodel import models

# from websocket import create_connection,warning
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
import random


class RecommendedResolution():
    def test(self):
        # 创建数据库对象
        recommendedItem = models.FootballWealthRecommend.objects.all()
        postItem = models.FootballWealthPost.objects.all()
        userItem = models.FootballWealthUser.objects
        resolutionItem = models.FootballWealthResolution.objects
        # 抽取亚盘比赛，进行解析
        for recommend in recommendedItem:
            resolution = {}
            resolution['id'] = recommend.id
            resolution['user_id'] = recommend.user_id
            resolution['post_id'] = recommend.post_id
            timeArray = time.localtime(int(int(recommend.create_time) / 1000))
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            resolution['create_time'] = otherStyleTime
            resolution['rr'] = recommend.rr
            resolution['sr'] = recommend.sr
            # 根据推荐ID获取所属poseId对应的user_name
            user_name = postItem.filter(post_id=recommend.post_id).values('username').first()
            if None == user_name:
                resolution['username'] = ''
            else:
                resolution['username'] = user_name['username']
            # 根据推荐ID获取所属poseId对应的vote_number
            vote_number = postItem.filter(post_id=recommend.post_id).values('week_vote_number').first()
            if None == vote_number:
                resolution['vote_number'] = 0
            else:
                resolution['vote_number'] = vote_number['week_vote_number']

            # 根据推荐ID获取所属poseId对应的content
            content = postItem.filter(post_id=recommend.post_id).values('content').first()
            if None == content:
                resolution['content'] = ''
            else:
                resolution['content'] = content['content']
            # 解析亚盘主受让
            if recommend.bd_yz_hjspl_checked == 1:
                resolution['recommended_str'] = str(recommend.league
                                                    + ' ' + str(recommend.match_time1)
                                                    + ' ' + str(recommend.match_time2)
                                                    + ' ' + recommend.home
                                                    + ' ' + str(recommend.homeScore)
                                                    + ' ' + str(recommend.awayScore)
                                                    + ' ' + recommend.away
                                                    + ' ' + recommend.yz_desc
                                                    + ' ' + recommend.bd_yz_hjspl_str
                                                    + ' ' + '@' + str(recommend.bd_yz_hjspl))
            # 解析亚盘客受让
            elif recommend.bd_yz_wjspl_checked == 1:
                resolution['recommended_str'] = str(recommend.league
                                                    + ' ' + recommend.match_time1
                                                    + ' ' + recommend.match_time2
                                                    + ' ' + recommend.home
                                                    + ' ' + recommend.homeScore
                                                    + ' ' + recommend.awayScore
                                                    + ' ' + recommend.away
                                                    + ' ' + recommend.yz_desc
                                                    + ' ' + recommend.bd_yz_wjspl_str
                                                    + ' ' + '@' + recommend.bd_yz_wjspl)

            # 解析让球负
            elif recommend.rq_rq0_checked == 1:
                resolution['recommended_str'] = str(recommend.match_id
                                                    + ' ' + recommend.home
                                                    + ' ' + str(recommend.homeScore)
                                                    + ' ' + str(recommend.awayScore)
                                                    + ' ' + recommend.away
                                                    + ' ' + recommend.letball
                                                    + '(' + recommend.rq_goal + ')' + ' 胜平负'
                                                    + ' 负' + recommend.rq_rq0
                                                    )
            # 解析让球平
            elif recommend.rq_rq1_checked == 1:
                resolution['recommended_str'] = str(recommend.match_id
                                                    + ' ' + recommend.home
                                                    + ' ' + str(recommend.homeScore)
                                                    + ' ' + str(recommend.awayScore)
                                                    + ' ' + recommend.away
                                                    + ' ' + recommend.letball
                                                    + '(' + recommend.rq_goal + ')' + ' 胜平负'
                                                    + ' 平' + recommend.rq_rq1
                                                    )
            # 解析让球胜
            elif recommend.rq_rq3_checked == 1:
                resolution['recommended_str'] = str(recommend.match_id
                                                    + ' ' + recommend.home
                                                    + ' ' + str(recommend.homeScore)
                                                    + ' ' + str(recommend.awayScore)
                                                    + ' ' + recommend.away
                                                    + ' ' + recommend.letball
                                                    + '(' + recommend.rq_goal + ')' + ' 胜平负'
                                                    + ' 胜' + recommend.rq_rq3
                                                    )
            # 解析胜平负负
            elif recommend.sf_sf0_checked == 1:
                resolution['recommended_str'] = str(recommend.match_id
                                                    + ' ' + recommend.home
                                                    + ' ' + str(recommend.homeScore)
                                                    + ' ' + str(recommend.awayScore)
                                                    + ' ' + recommend.away
                                                    + ' 胜平负'
                                                    + ' 负' + recommend.sf_sf0
                                                    )
            # 解析胜平负平
            elif recommend.sf_sf1_checked == 1:
                resolution['recommended_str'] = str(recommend.match_id
                                                    + ' ' + recommend.home
                                                    + ' ' + str(recommend.homeScore)
                                                    + ' ' + str(recommend.awayScore)
                                                    + ' ' + recommend.away
                                                    + ' 胜平负'
                                                    + ' 平' + recommend.sf_sf1
                                                    )
            # 解析胜平负胜
            elif recommend.sf_sf1_checked == 3:
                resolution['recommended_str'] = str(recommend.match_id
                                                    + ' ' + recommend.home
                                                    + ' ' + str(recommend.homeScore)
                                                    + ' ' + str(recommend.awayScore)
                                                    + ' ' + recommend.away
                                                    + ' 胜平负'
                                                    + ' 胜' + recommend.sf_sf3
                                                    )
            # 解析大小球主受让
            elif recommend.dxq_hjspl_checked == 1:
                resolution['recommended_str'] = str(recommend.league
                                                    + ' ' + recommend.match_time1
                                                    + ' ' + recommend.match_time2
                                                    + ' ' + recommend.home
                                                    + ' ' + str(recommend.homeScore)
                                                    + ' ' + str(recommend.awayScore)
                                                    + ' ' + recommend.away
                                                    + ' ' + recommend.dxq_desc
                                                    + ' ' + recommend.dxq_hjspl_str
                                                    + ' @' + recommend.dxq_hjspl
                                                    )
            # 解析大小球客受让
            elif recommend.dxq_wjspl_checked == 1:
                resolution['recommended_str'] = str(recommend.league
                                                    + ' ' + recommend.match_time1
                                                    + ' ' + recommend.match_time2
                                                    + ' ' + recommend.home
                                                    + ' ' + str(recommend.homeScore)
                                                    + ' ' + str(recommend.awayScore)
                                                    + ' ' + recommend.away
                                                    + ' ' + recommend.dxq_desc
                                                    + ' ' + recommend.dxq_wjspl_str
                                                    + ' @' + recommend.dxq_wjspl
                                                    )
            else:
                resolution['recommended_str'] = '暂未解析'
            # 存入数据库

            try:
                resolutionItem.get(id=resolution['id'])
                resolutionItem.filter(id=resolution['id']).update(**resolution)
            except:

                resolutionItem.create(**resolution)


if __name__ == "__main__":
    data = RecommendedResolution()
    data.test()

    # timeArray = time.localtime(time.time())
    # otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    # print(time.time())
    # print(timeArray)
    # print(otherStyleTime)
