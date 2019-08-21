#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/25 8:52
# @Author  : Lares
# @Software: PyCharm

# 下载百度首页的logo图片
# https://www.baidu.com/img/bd_logo1.png


import socket
import re

# 创建客户端
client = socket.socket()  # socket对象，用来和服务端建立连接

# 连接服务端   connect接收的是一个元组，只能接收一个元组
# client.connect(('IP/域名',http协议端口号))
client.connect(('www.baidu.com',80))
# 构造http报文
# b'请求方法 URL HTTP/1.0\r\nHost: 服务端\r\n\r\n'
request = b'GET /img/bd_logo1.png HTTP/1.0\r\nHost: www.baidu.com\r\n\r\n'
# 发送报文
client.send(request)

# 接收响应数据  第一次，包含响应头
data = client.recv(1024)

# 接收图片信息变量
res = b''


while data:
    res += data
    data = client.recv(512)

# 创建图片文件
with open('bd_logo1.png','wb') as f:
    f.write(re.findall(b'\r\n\r\n(.*)',res,re.S)[0])

# print(res)