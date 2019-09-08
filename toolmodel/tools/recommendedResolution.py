import sys
import os
import django
import logging

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
        # 抽取亚盘比赛，进行解析
        for recommend in recommendedItem:
            if recommend.bd_yz_hjspl_checked == 1:
                print(recommend.league, recommend.match_time1, recommend.match_time2, recommend.home,
                      recommend.homeScore, recommend.awayScore, recommend.away, recommend.yz_desc,
                      recommend.bd_yz_hjspl_str, '@',recommend.bd_yz_hjspl)
            elif recommend.bd_yz_wjspl_checked == 1:
                print(recommend.league, recommend.match_time1, recommend.match_time2, recommend.home,
                      recommend.homeScore, recommend.awayScore, recommend.away, recommend.yz_desc,
                      recommend.bd_yz_wjspl_str, '@', recommend.bd_yz_wjspl)


if __name__ == "__main__":
    data = RecommendedResolution()
    data.test()
