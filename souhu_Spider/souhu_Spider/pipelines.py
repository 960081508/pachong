# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class QuanshuPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonPipeline(object):
    def __init__(self):
        self.file = open('souhu.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.file.write(line.encode('utf-8'))
        return item
