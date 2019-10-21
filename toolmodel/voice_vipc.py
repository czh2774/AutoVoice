#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import socket
import os
import sys
import django

import threading
from websocket import create_connection
sys.path.append(os.path.abspath('..'))  # 将项目路径添加到系统搜寻路径当中
os.environ['DJANGO_SETTINGS_MODULE'] = 'AutoVoice.settings'  # 设置项目的配置文件
django.setup()
import time, json, requests
from toolmodel import models

# from websocket import create_connection,warning
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
import random

"""创建异常类"""


class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg


"""喊话器支持工具"""


class voice_tool():
    def get_ip(self):
        """获取代理IP"""
        ob = models.proxyip.objects
        logging.info('开始获取代理IP')
        try:
            url = 'http://api3.xiguadaili.com/ip/?'
            param = {'tid': 557103946283937,
                     'num': 100,
                     'delay': 50,
                     'category': 2,
                     'longlife': 10,
                     'filter': 'on',
                     'protocol': 'https',
                     'format': 'json'
                     }

            data = requests.get(url=url, params=param).text
        except:
            logging.warning('请求获取代理失败,重新请求')
            self.get_ip()
        logging.info('获取代理IP成功 %s', data)
        data = json.loads(data)

        for proxy in data:
            logging.info(proxy)
            proxy_host_http = 'http://' + str(proxy['host']) + ':' + str(proxy['port'])
            proxy_host_https = 'https://' + str(proxy['host']) + ':' + str(proxy['port'])
            proxy_http_http = {
                'http': proxy_host_http,
                'https': proxy_host_https
            }
            proxy_http_http = str(proxy_http_http).replace("'", '"')
            proxy['proxy_http_http'] = proxy_http_http

            logging.info(proxy)
            ob.create(**proxy)

    def check_ip(self):
        """检查代理IP高匿性"""
        ob = models.proxyip.objects
        data = ob.all()
        p = ''
        for proxy in data:
            proxy_http_http = proxy.proxy_http_http
            proxy_http_http = json.loads(proxy_http_http)

            try:

                logging.info('开始检查代理')
                '''head 信息'''
                head = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
                    'Connection': 'keep-alive'}

                '''http://icanhazip.com会返回当前的IP地址'''
                p = requests.get('http://icanhazip.com', headers=head, proxies=proxy_http_http, timeout=4).text
                logging.debug(p)
                target = ob.filter(host=proxy.host)
                if proxy.host in p:

                    logging.debug('检查目标%s', data)
                    logging.debug(p)
                    logging.debug('校验高匿成功%s', data)
                    target.update(hiding=1)
                else:
                    logging.debug('校验高匿失败，删除本条记录，检查下一个%s', p)

                    target.delete()
            except:
                logging.debug('错误，检查下一个')
                target = ob.filter(host=proxy.host)
                target.delete()
                pass


"""获取房间列表工具"""


class rid_list():
    def match_list(self):

        """获取比赛列表"""
        try:
            logging.info('开始获取比赛数据')
            url = 'https://i-live.vipc.cn/api/home/v2/football/date/today/next'
            headers = {'If-None-Match': 'W/"1a8b-6BaO4mqgB5V9sw1WDfNMBJ2Obqc"', 'Host': 'i-live.vipc.cn',
                       'Connection': 'close', 'Accept-Encoding': 'gzip, deflate', 'User-Agent': 'gzip'}
            data = requests.get(url=url, headers=headers)
            data = data.text
            # logging.info(data)
            data = json.loads(data)
            data = data['items']
            data.pop(0)
            match_list_data = []
            for i in data:
                i = i['matches']
                for j in i:
                    logging.debug(j)
                    match_list_data.append(j['model']['matchId'])
        except:
            logging.warning('获取比赛列表出错,重新获取')
            self.match_list()
        return match_list_data

    def get_rid_list(self):
        """"获取直播间数据"""
        match_list = self.match_list()
        logging.info('准备获取直播间数据')
        logging.debug(match_list)
        rid = {}  # rid数据
        count = 0
        rid_count = 0
        ob = models.rid.objects
        ob.all().delete()
        for j in match_list:
            logging.debug('目标%s', j)
            try:
                logging.debug(j)
                url = 'https://i-live.vipc.cn/api/football/' + str(j)
                headers = {'If-None-Match': 'W/"511-0OHFh71eTNfzg6vgrBMPmyFurtc"', 'Host': 'i-live.vipc.cn',
                           'Connection': 'close', 'Accept-Encoding': 'gzip, deflate', 'User-Agent': 'gzip'}
                data = json.loads(requests.get(url=url, headers=headers).text)
            except:
                logging.warning('获取%s直播间数据出错,继续下一个', j)
                continue
                # self.get_rid_list()
            logging.debug('直播间数据：%s', data)
            count = count + 1
            if 'room' in data and 'endTime' not in data['room'] and data['room']['chatCount'] > 20:
                rid['rid'] = data['room']['_id']
                rid['chatCount'] = data['room']['chatCount']
                rid['home'] = data['model']['home']
                rid['guest'] = data['model']['guest']
                rid_count = rid_count + 1
                try:
                    ob.get(rid=rid['rid'])
                    logging.info('有这个数据')
                    ob.filter(rid=rid['rid']).update(chatCount=rid['chatCount'])
                except:
                    logging.info('没有这个数据')
                    ob.create(**rid)

            logging.info('本次需要获取直播间数据%s,当前已获取%s', len(match_list), count)

        logging.info('本次获取直播间数据数据%d', rid_count)
        if rid_count == 0:
            logging.info('本次数据获取为%s,重新获取', rid_count)
            self.get_rid_list()


"""喊话器主函数"""


class voice_vipc():
    closure = 0  # 是否被封号
    """获取mobile,cookie函数"""

    def mobile_cookie_get(self):
        logging.info('开始初始化数据')
        ob = models.user.objects
        ob.filter(isdead=1).delete()

        """获取一个未使用的，还活着的cookies"""
        cookie_ob = ob.all().first()
        count_mobile = 0
        while count_mobile < 5:
            logging.info('正在从数据库第%d次获取mobile和cookies', count_mobile)
            if cookie_ob:
                mobile = cookie_ob.mobile
                cookies = {}
                cookies['; uid'] = cookie_ob.user_id
                cookies['utk'] = cookie_ob.utk
                cookies['nutk'] = cookie_ob.nutk
                cookies['vid'] = '5bdb38a79e2238001a3d0511'
                cookies['imei'] = '865166026327588'
                cookies['app'] = 'vipc-android'
                cookies['chnl'] = 'officer'
                cookies['ver'] = '5.6.4'
                mobile = mobile
                logging.info('初始化数据完毕，获取手机号 %s,获取cookie %s', mobile, cookies)
                break
            else:
                logging.error('没有mobile可用了')
        return mobile, cookies

    """喊话器主函数"""

    def voice_room(self):
        """确定models"""
        ob_note_list = models.note.objects
        ob_rid_list = models.rid.objects
        ob_proxy_list = models.proxyip.objects
        ob_user_list = models.user.objects
        ob_log_list = models.log_voice.objects
        """获取直播间数据"""
        rid_list = []
        count_rid = 0

        while count_rid < 240:
            count_rid = count_rid + 1
            try:

                rid_list = ob_rid_list.all()  # 获取直播间列表
                logging.info('从数据库中获取直播间数据第%s次', count_rid)
                if rid_list:
                    break
                else:
                    logging.info('目前没有满足条件的直播间，休息1分钟')
                    time.sleep(60)
            except:
                logging.error('获取直播间数据失败')
                break
        logging.info('目标直播间%d个，列表%s', len(rid_list), rid_list)
        """获取mobile和cookie数"""
        mobile_cookie = {}
        mobile_cookie = self.mobile_cookie_get()  # 获取本次使用的mobile和cookie
        logging.info('本次使用的mobile,cookie %s', mobile_cookie)
        cookie = ('; uid=' + mobile_cookie[1]['; uid']
                  + '; utk=' + mobile_cookie[1]['utk']
                  + '; nutk=' + mobile_cookie[1]['nutk']
                  + '; vid=' + mobile_cookie[1]['vid']
                  + '; imei=865166026327588; app=vipc-android; chnl=Vipc-MTwdj; ver=5.7.3;')
        """获取话术数据"""

        note_ob_list = ob_note_list.all().filter(isdead=None)

        logging.info('本次使用的广告语列表%s,广告语数量%d', type(note_ob_list), len(note_ob_list))

        """对所有房间进行喊话"""

        for j in rid_list:
            """初始化参数"""

            """初始化统计日志"""
            effect_log = {}
            effect_log['rid_list'] = {}
            effect_log['note_list'] = []
            effect_log['send_list'] = []

            effect_log['user'] = ''
            """初始化本轮话术"""
            note_ob = note_ob_list[random.randint(0, len(note_ob_list) - 1)]
            note_list = [note_ob.note1, note_ob.note2, note_ob.note3, note_ob.note4]
            effect_log['user'] = note_ob.user

            """本次喊话目标"""
            logging.info('本次喊话目标主 %s，客 %s，直播间人数%s,rid %s', j.home, j.guest, j.chatCount, j.rid)
            logging.info('本次喊话话术%s', note_list)

            for i in range(5):
                try:
                    proxy = ob_proxy_list.filter(hiding=1).first()
                    logging.info('本次使用的代理是%s:%s', proxy.host, proxy.port)
                    logging.info('准备进入直播间 %s对 %s，直播间人数%s,rid %s', j.home, j.guest, j.chatCount, j.rid)
                except:
                    logging.info('获取代理出错')
                    continue
                try:
                    ws = create_connection(
                        "ws://live.vipc.cn/socket.io/?EIO=3&transport=websocket",
                        cookie=cookie,
                        http_proxy_host=proxy.host,
                        http_proxy_port=proxy.port,
                        timeout=60
                    )
                    break
                except:
                    logging.info('连接房间失败，重试第%d次,删除代理%s', int(i + 1), str(proxy.host))
                    proxy.delete()

                    ob_log_list.create(**{'log_title': '代理超时删除代理', 'log_data': str(proxy.host)})

            """发送进入房间数据"""
            ws.send('40/live,')
            ws.send('42/live,["\/room\/enter",{"rid":"' + j.rid + '"}]')
            ws.send('2')
            effect_log['rid_list'] = {'home': j.home, 'guest': j.guest}
            """心跳线程函数"""

            def live_voice(threadName, delay):
                logging.info('开始心跳')
                for i in range(5):
                    ws.send('2')
                    logging.debug('发送心跳包')
                    time.sleep(delay)

            """接收数据函数"""

            def result_voict(threadName, delay):
                logging.info('开始接收数据')
                count = 0
                try:
                    while count < 30:
                        time.sleep(delay)
                        result = ws.recv()
                        if result:
                            count = count + 1
                            logging.info('目前已接收%s,接收信息%s', count, result)

                            for l in note_list:
                                """检查"""
                                if '42/live,["/chat/message"' in result and str(l) in result:
                                    logging.info(result)
                                    effect_log['note_list'].append(l)
                                    logging.info('成功发出文字列表%s', str(effect_log['note_list']))

                            if '抱歉，您的评论内容涉嫌违规，已被禁止发表评论' in result:
                                logging.info('出错, %s已被封禁,%s代理已被封禁，删除重新开始', mobile_cookie[0], proxy.host)

                                ob_user_list.all().filter(mobile=mobile_cookie[0]).delete()
                                ob_log_list.create(**{'log_title': '账号被封，删除手机数据', 'log_data': str(mobile_cookie[0])})
                                ob_proxy_list.all().filter(host=proxy.host).delete()
                                ob_log_list.create(
                                    **{'log_title': '账号被封，删除代理数据', 'log_data': str(proxy.host + ':' + proxy.port)})
                                raise Networkerror('isdead_user')

                            if '直播间不存在或已结束' in result:
                                logging.info("%s 对阵 %s 的直播间已经结束", j.home, j.guest)
                                raise Networkerror('直播间已经结束')
                                ws.close()
                    logging.info('接收数据超过上限，关闭连接')
                except Networkerror as e:
                    logging.info('账号被封')
                    time.sleep(1200)
                    logging.info('休息%d秒', 1200)

                except:
                    ws.close()

                ws.close()

            """发送广告线程"""

            def note_voice(threadName, delay):

                send_sequence = 0
                for k in note_list:
                    if k:
                        send_cookie = {}
                        send_cookie['uid'] = mobile_cookie[1]['; uid']
                        send_cookie['utk'] = mobile_cookie[1]['utk']
                        send_cookie['vid'] = "5bdb38a79e2238001a3d0511"
                        send_cookie['rid'] = j.rid
                        send_cookie['t'] = 0
                        send_cookie['c'] = {'m': k}
                        send_str = '42/live,' + str(send_sequence) + '["\/chat\/message\/create",' + str(
                            send_cookie) + ']'
                        send_str = send_str.replace("'", '"')
                        time.sleep(10)
                        logging.info('发送广告%s', send_str)
                        send_sequence = send_sequence + 1
                        ws.send(send_str)
                        effect_log['send_list'].append(k)
                        time.sleep(delay)

            """启动线程"""
            s1 = threading.Thread(target=result_voict, args=('接收', 0.2))
            s2 = threading.Thread(target=live_voice, args=("心跳包", 25))
            s3 = threading.Thread(target=note_voice, args=("发送广告", 4))
            s1.start()
            s2.start()
            s3.start()
            s1.join()
            s2.join()
            s3.join()
            """输出结果到日志"""
            ob_log_list.create(**{'log_title': '喊话', 'log_data': str(effect_log)})

        self.voice_room()


if __name__ == "__main__":
    # ob_note_list = models.note.objects
    # ob_rid_list = models.rid.objects
    # ob_proxy_list = models.proxyip.objects
    # ob_user_list = models.user.objects
    ob_log_list = models.log_voice.objects
    data = voice_tool()
    data.get_ip()
    data.check_ip()
    # ob_rid_list = models.rid.objects

    # room=rid_list()
    # room.get_rid_list()
    # ob_rid_list = models.rid.objects
    # rid_list = ob_rid_list.all()  # 获取直播间列表
    # logging.info(rid_list)
    # ob_user_list=models.user.objects
    # ob_user_list.all().filter(mobile=13945894862).delete()
