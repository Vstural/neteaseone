# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class EasePipeline(object):
    def process_item(self, item, spider):
    	print "*************************"
    	print item['goods_pic_url'].decode()
    	print item['intro_pic_urls']
    	print item[u'item_name']
    	print item['file_id']
    	print "*************************"

        return item
