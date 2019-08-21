#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 8:42
# @Author  : Lares
# @Software: PyCharm


# 全书网小说爬虫,爬取一部小说的简介信息,如作者,类型,名称,当前连载状态等,存入txt文件中.
# http://www.quanshuwang.com/
# http://www.quanshuwang.com/book_9055.html

import requests
from lxml import html
from lxml import etree

html_doc = requests.get('http://www.quanshuwang.com/book_9055.html').content.decode('gbk')

html = etree.HTML(html_doc)

# print(html)
leixing = html.xpath('//a[contains(@class,"c009900")]/text()')[0]

title_book = html.xpath('//h1/text()')[0]

zt = html.xpath('//dl[1]/dd/text()')[0]

author = html.xpath('//dl[2]/dd/text()')[0]

info_book = html.xpath('//div[contains(@id,"waa")]/text()')[0]

dm = '作品：{}\n作者：{}\n类型：{}\n连载状态：{}\n{}\n'.format(title_book,author,leixing,zt,info_book)

print(dm)