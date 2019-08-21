#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/10 10:19
# @Author  : Lares
# @Software: PyCharm

# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
from selenium import  webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get('https://www.baidu.com')
html = driver.page_source
print(html)


