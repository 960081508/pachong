# -*- coding: utf-8 -*-

import scrapy
from ..items import AreaItem

# https://www.aqistudy.cn/historydata/
# 从https://www.aqistudy.cn/historydata/页面开始
# 获取所有城市每一天的数据，每个城市可以只需要一个月的数据

class AreaSpiderSpider(scrapy.Spider):
    name = 'area_spider'
    # allowed_domains = ['dddd']
    start_urls = ['https://www.aqistudy.cn/historydata/']
    base_urls = 'https://www.aqistudy.cn/historydata/'


    def parse(self, response):
        '''
        匹配城市详情页
        :param response:
        :return:
        '''
        # 匹配城市URL
        city_url = response.xpath('//div[@class = "all"]/div[2]/ul/div[2]/li/a/@href').extract()
        # 匹配城市名字
        city_name = response.xpath('//div[@class = "all"]/div[2]/ul/div[2]/li/a/text()').extract()
        print('正在解析每个城市的URL链接')
        for url,name in zip(city_url,city_name):
            yield scrapy.Request(url='{}{}'.format(self.base_urls,url),callback=self.parse_month,meta={'city_name':name})


    def parse_month(self,response):
        '''
        匹配月份详情页
        :param response:
        :return:
        '''
        # 匹配月份URL
        month_url = response.xpath('//ul[@class = "unstyled1"]/li/a/@href').extract()
        print('正在解析每个城市每月的URL链接')
        for url in month_url:
            yield scrapy.Request(url='{}{}'.format(self.base_urls,url),callback=self.parse_day,meta={'driver':True,'city_name':response.meta.get('city_name')})


    def parse_day(self,response):
        '''
        匹配每一天的详细数据
        :param response:
        :return:
        '''
        city_name = response.meta.get('city_name','未知')
        print('正在解析{}每一天的详细数据'.format(city_name))
        items_list = response.xpath('//tr')
        items_list.pop(0)   # 删除表头

        print(items_list)
        for item in items_list:
            items = AreaItem()
            # 匹配城市
            items['city'] = city_name
            # 匹配日期
            items['date'] = item.xpath('./td[1]/text()').extract_first()
            # 匹配空气质量指数
            items['aqi'] = item.xpath('./td[2]/text()').extract_first()
            # 匹配空气质量等级
            items['level'] = item.xpath('./td[3]/span/text()').extract_first()

            yield items