# IP地址取自国内髙匿代理IP网站：http://www.xicidaili.com/nn/
# 仅仅爬取首页IP地址就足够一般使用


import requests,json


def get_ip():
    url = 'http://api3.xiguadaili.com/ip/'
    params={'tid':556879104307837,'num':1,'exclude_ports':8000,'delay':100,'longlife':60,'format':'json','filter':'on'}
    response=requests.get(params=params,url=url)
    response=response.text
    #response=json.loads(response)
    print(response)
    #return response.text
if __name__ == '__main__':


    proxies = get_ip()
    #print(proxies)
