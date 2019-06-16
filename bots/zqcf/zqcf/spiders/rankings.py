import scrapy
from bots.zqcf.zqcf.items import ZqcfItem

import os
import sys

class rankingsSpider(scrapy.Spider):
    name='rankingsSpider'
    start_urls=['https://appbalance.zqcf718.com/vote/rankings',]
    def parse(self, response):

        return scrapy.Request(url='https://appbalance.zqcf718.com/vote/rankings',
                              method='POST',
                              headers={'Content-Type': 'application/json; charset=utf-8',
                                       'Content-Length': '135',
                                       'Host': 'appbalance.zqcf718.com',
                                       'Connection': 'Keep-Alive',
                                       'Accept-Encoding': 'gzip',
                                       'User-Agent': 'okhttp/3.12.0'
                                       },
                              body={"params":
                                              {"type":"0","v":"1","platform":"android",
                                               "version_code":"8","device_type":"1",
                                               "device_id":"861759031464380","version":"2.0"
                                               }
                                     })

