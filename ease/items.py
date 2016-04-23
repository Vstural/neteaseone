# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EaseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    goods_pic_url = scrapy.Field()
    intro_pic_urls = scrapy.Field()
    item_name = scrapy.Field()
    file_id = scrapy.Field()
    total_need = scrapy.Field()
    