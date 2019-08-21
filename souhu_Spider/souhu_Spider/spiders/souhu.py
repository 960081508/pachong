# -*- coding: utf-8 -*-

# 1.通过Crawlspider 请求 http://www.sohu.com/新闻页面.
# 要求: 通过定义rule规则,提取首页和详情页面的文章url,以及匹配详情页面的字段数据

import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SouhuSpider(CrawlSpider):
    name = 'souhu'
    # allowed_domains = ['http://www.sohu.com/']
    start_urls = ['http://www.sohu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.sohu.com/a/.*?'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        '''
        匹配详情页数据
        :param response:
        :return:
        '''
        title = response.xpath('//h1/text()').extract()
        # title_str = title.split('')
        # print(title)
        time = response.xpath('//span[@class="time"]/text()').extract()
        # print(time)
        article = response.xpath('//article[@class="article"]/p/text()').extract()
        # print(article)

        yield {
            'title':title,
            'time':time,
            'article':article
        }
