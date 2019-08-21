#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/10 9:18
# @Author  : Lares
# @Software: PyCharm


import re
import requests

start_url ='https://github.com/session'
login_url = 'https://github.com/session'

session = requests.session()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    'Referer': 'https://github.com/login',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host':'github.com',
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    'Origin': 'https://github.com',
}

resp = session.get(start_url,headers=headers,verify=False).text
token = re.findall(r' name="authenticity_token" value="(.*?)" />',resp,re.S)

authenticity_token = None
if token:
    authenticity_token = token[0]
    print('token获取成功：',authenticity_token)

data ={
    'commit': 'Sign in',
    'utf8': '✓',
    'authenticity_token':authenticity_token,
    'login': '960081508@qq.com',
    'password':'cmhbf9600',
    'webauthn-support': 'supported',
}

r = session.post(login_url,data=data,headers=headers,verify=False).text

with open('login_res.html','w',encoding='utf-8') as f:
    f.write(r)

