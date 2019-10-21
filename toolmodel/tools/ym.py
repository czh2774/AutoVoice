#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import time, re

username = 'czh2774'
password = 'Zhangquan1'
UserLoginStr_url = 'http://dkh.d1tm.com/service.asmx/UserLoginStr'  # 登录URL
GetHM2Str_url = 'http://dkh.d1tm.com/service.asmx/GetHM2Str'  # 获取手机号URL
GetYzm2Str_url = 'http://dkh.d1tm.com/service.asmx/GetYzm2Str'  # 获取验证码URL
xmid = 2529


class ym_data():
    def __init__(self):
        self.token = self.get_info()

    def get_info(self):
        data = {'name': 'czh2774', 'psw': 'Zhangquan1'}
        value = requests.get(url=UserLoginStr_url, params=data)
        value = value.text
        print(value)
        return value

    def get_mobile(self):
        print('正在获取手机号>>>>>>>')
        params = {'token': self.token,
                  'xmid': xmid,
                  'a1': '',
                  'a2': '',
                  'sl': 1,
                  'lx': 6,
                  'pk': '',
                  'ks': 0,
                  'rj': ''}
        value = requests.get(url=GetHM2Str_url, params=params)
        value = value.text
        print(value)
        value = value.split('=')
        value = value[1]
        print('<<<<<<获取手机号', value)
        return value

    def get_release(self, mobile):
        value = '1'
        data = {'token': self.token, 'xmid': xmid, 'hm': mobile, 'sf': 1}
        times = 0
        while value == '1' and times < 12:
            times = times + 1
            print('开始获取验证码>>>>>>', times)
            value = requests.get(url=GetYzm2Str_url, params=data)
            print('等待5秒>>>>>>')
            time.sleep(5)
            # value.encoding = value.apparent_encoding
            value = value.text
            print('<<<<<<验证码JSON:', value)
        if '验证码' in value:
            data = re.sub("\D", "", value[19:])
            print('<<<<<<验证码JSON:', data)
        return data


if __name__ == '__main__':
    data = ym_data()
    # data.get_mobile()
    value = data.get_release(data.get_mobile())
    # data='success|【唯彩会】验证码：2684，用于注册唯彩看球账户，若非本人操作请忽略（本短信免费）'
    # data=re.sub("\D", "", data)
    # print(data)
