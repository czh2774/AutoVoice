# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy_djangoitem import DjangoItem
from toolmodel import models

class ZqcfPipeline(object):
    def process_item(self, item, spider):

        db = models.zuqiumofang_user.objects
        db.update_or_create(defaults=item, user_id=item['user_id'])
        return item
