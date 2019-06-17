import scrapy
import json
from scrapy import Request
from scrapy.spiders import  CrawlSpider




class rankSpider(CrawlSpider):

    name='rank'
    method='POST'
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    body = {
        'params':
                {
                    "type": "0", "v": "1",
                 "platform": "android","version_code": "8",
                 "device_type": "1","device_id": "861759031464380",
                 "version": "2.0"
                 }
            }


    def start_requests(self):
        yield Request(url='https://appbalance.zqcf718.com/vote/rankings',method='POST',headers=self.headers,body=json.dumps(self.body),callback=self.parse)
    def parse(self, response):
        value=json.loads(response.text)
        value = value['data']
        value = iter(value)  #
        ranking = 0  # 初始化排名数据
        """遍历迭代器
        如果user_id不存在，就创建，并且从未使用的nickname中获取一个最新的作为nickname，
        rankings为当前排序。
        如果user_id存在，就覆盖，rankings为当前排序"""
        item={}
        for item in value:
            ranking = ranking + 1
            item['ranking'] = ranking

            yield item


