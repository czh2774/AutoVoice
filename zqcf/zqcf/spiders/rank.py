import scrapy
import json
from scrapy.http import FormRequest
from scrapy.spiders import  CrawlSpider
import sys
from ..items import ZqcfItem



class rankSpider(CrawlSpider):
    name='rank'
    method='POST'
    headers = {'Content-Type': 'application/json',
                               'charset':'utf-8',
               'Content-Length': '135',
               'Host': 'appbalance.zqcf718.com',
               'Connection': 'Keep-Alive',
               'Accept-Encoding': 'gzip',
               'User-Agent': 'okhttp/3.12.0'
               }
    body = {"params":
                {"type": "0", "v": "1", "platform": "android",
                 "version_code": "8", "device_type": "1",
                 "device_id": "861759031464380", "version": "2.0"
                 }
            }
    def start_requests(self):
        yield FormRequest(url='https://appbalance.zqcf718.com/vote/rankings',headers=self.headers,formdata=self.body,callback=self.parse)
    def parse(self, response):
        #print(response)
        pass
