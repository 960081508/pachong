#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/26 9:53
# @Author  : Lares
# @Software: PyCharm

# https://image.baidu.com/search/acjson?tn=resultjson_com&catename=pcindexhot&ipn=rj&ct=201326592&is=&fp=result&queryWord=&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=pcindexhot&face=0&istype=2&qc=&nc=1&fr=&pn=0&rn=30

import urllib
import urllib.request
import re


url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&catename=pcindexhot&ipn=rj&ct=201326592&is=&fp=result&queryWord=&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=pcindexhot&face=0&istype=2&qc=&nc=1&fr=&pn=0&rn=30'
# s = urllib.request.urlopen(url)
headers = {
    # 用户信息
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    # 从百度图片网址跳转过来
}

# 这里写爬虫的请求头
res = urllib.request.Request(url,headers=headers)

s = urllib.request.urlopen(res).read().decode()

# s = body.read().decode("utf-8")
# print(res)
# print(s)

# 正则取出图片链接
key = r'"thumbURL":"(.+?)"'
pic = re.compile(key)
num = 1
# 循环遍历输出图片链接
for i in re.findall(pic,s):
    print(i)
    f_res = urllib.request.Request(i,headers=headers)
    f_body = urllib.request.urlopen(f_res).read()       # 读取图片的内容
    f = open(r'C:\Users\Administrator\Desktop\class45\pachong\img\ '+ str(num) + '.jpg','wb+')  # 以二进制创建或打开一个jpg文件
    f.write(f_body) # 往文件里写入内容
    f.close() # 关闭文件
    num += 1

