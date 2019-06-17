# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


from scrapy_djangoitem import DjangoItem
from ToolModel.models import zuqiumofang_user,zuqiumofang_post,zuqiumofang_tuijian

class rankItem(DjangoItem):
    django_model = zuqiumofang_user

class postlistItem(DjangoItem):
    django_model = zuqiumofang_post

class tuijianItem(DjangoItem):
    django_model = zuqiumofang_tuijian