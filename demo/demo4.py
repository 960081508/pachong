#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/28 9:16
# @Author  : Lares
# @Software: PyCharm


# https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85&pn=0      pn=每翻一页+50

import re
import requests

session = requests.session()

# i = 0

# urls = 'https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85&ie=utf-8&pn={}'.format(str(i))

urls = 'https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85'


# for i in urls:
#     if i != str(200):
res = session.get(urls).text
        # 匹配帖子的详情页
article_urls = re.findall(r'<a rel="noreferrer" href="/p/\d+"',res,re.S)
        # 匹配帖子的作者
article_author = re.findall(r'title="主题作者:(.*?)"',res,re.S)
for url,author in zip(article_urls,article_author):
    article_res = session.get('https://tieba.baidu.com{}'.format(url)).text
    title = re.findall(r"'threadTitle': '(.*?)'",article_res,re.S)
    push_time = re.findall(r'<span class="tail-info">1楼</span><span class="tail-info">(.*?)</span>',article_res,re.S)
    if title and push_time:
        print('主题:{},楼主:{},发帖时间:{}'.format(title[0],author,push_time))
        print('-------------------------------------')

    # i += 50