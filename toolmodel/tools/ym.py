#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import time,re
username='czh2774'
password='Zhangquan1'
token='00946939f7b89eeab6999ccf00b87a0afe5042297701'
url='http://api.fxhyd.cn/UserInterface.aspx'
itemid=239
class ym_data():
    def get_info(self):
        action='getaccountinfo'
        data={'action':action,'token':token,'format':1}
        #print(data)
        value=requests.get(url=url,params=data)
        value=value.text
        return value
    def get_mobile(self):
        print('正在获取手机号>>>>>>>')
        action = 'getmobile'
        data = {'action': action, 'token': token, 'itemid':itemid}
        #print(data)
        value = requests.get(url=url, params=data)
        value = value.text
        value=value.split('|')
        value=value[1]
        print('<<<<<<获取手机号',value)
        return value
    def get_release(self,mobile):
        action='getsms'
        value='3001'
        #print(self.get_mobile())
        data = {'action': action, 'token': token, 'itemid': itemid, 'mobile': mobile}
        times=0
        while value=='3001' and times<12:
            times=times+1
            print('开始获取验证码>>>>>>',times)

            value=requests.get(url=url,params=data)

            print('等待5秒>>>>>>')
            time.sleep(5)
            print(value)
            value.encoding=value.apparent_encoding
            value=value.text
            print('<<<<<<验证码JSON:',value)
        return value
if __name__ == '__main__':
    data=ym_data()
    #data.get_mobile()
    #value=data.get_release(data.get_mobile())
    # data='success|【唯彩会】验证码：2684，用于注册唯彩看球账户，若非本人操作请忽略（本短信免费）'
    # data=re.sub("\D", "", data)
    # print(data)