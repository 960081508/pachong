# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

# 通过scrapy获取全书网小说的多个字段信息，如名字 作者等，通过pipelines保存为json文件

import scrapy


class QsSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 书名
    book_name = scrapy.Field()
    # 简介
    content = scrapy.Field()
    # 作者
    author = scrapy.Field()