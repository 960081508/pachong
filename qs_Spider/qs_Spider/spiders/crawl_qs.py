# -*- coding: utf-8 -*-
import scrapy
from ..items import QsSpiderItem


class CrawlQsSpider(scrapy.Spider):
    # 属性 爬虫文件代码的名字 具有唯一性
    name = 'crawl_qs'
    # 定义抓取范围
    # allowed_domains = ['www.quanshuwang.com']
    # 初始请求的URL地址
    start_urls = ['http://www.quanshuwang.com/']



    def parse(self, response):
        '''
        匹配书籍详情页URL
        :param response:
        :return:
        '''
        # ul class = b-all-content cf
        detail_urls = response.xpath('//ul[@class="b-all-content cf"]/li/a[1]/@href').extract()

        for url in detail_urls:
            yield scrapy.Request(url=url,callback=self.parse_response)

        # next_url =

    def parse_response(self,response):
        '''
        匹配详情页具体字段信息
        :param response:
        :return:
        '''

        content = response.xpath('//div[@id = "waa"]/text()').extract()
        print(content)
        # print(content)
        book_name = response.xpath('//h1/text()').extract()
        print(book_name)
