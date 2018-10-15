# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QingguoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    novel_name = scrapy.Field()
    novel_author = scrapy.Field()
    novel_tag = scrapy.Field()
    novel_zishu = scrapy.Field()
    novel_redu = scrapy.Field()
    novel_shoucang = scrapy.Field()
    novel_status = scrapy.Field()
    novel_introduction = scrapy.Field()
    novel_startdate = scrapy.Field()
    novel_updatedate = scrapy.Field()
    novel_url = scrapy.Field()
    pass
