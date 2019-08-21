# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AreaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 日期
    date = scrapy.Field()
    # 空气质量指数
    aqi = scrapy.Field()
    # 空气质量等级
    level = scrapy.Field()
