# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
import os
import utils
import json
save_path = 'C:\\Users\\Nzeli\\Desktop\\save\\'

class EasePipeline(object):
    def process_item(self, item, spider):
    	# print "*************************"
    	# print item['goods_pic_url'].decode()
    	# print item['intro_pic_urls']
    	# print item['item_name']
    	# print item['file_id']
    	# print item['total_need']
    	# print item['file_id']+item['goods_pic_url'][:4]
    	# print item['file_id']
    	# print item['goods_pic_url']
    	# print item['goods_pic_url'][:4]
    	# print "*************************"
    	path = save_path+item['file_id'] + '\\' 
    	try:
    		os.mkdir(path)
    	except Exception,e:
    		print("file existed")

    	with open(path + 'item.json','wb') as json_file:
    		data = dict(item)
    		json.dump(data, json_file)

    	utils.downloadImg(path, item['goods_pic_url'],item['file_id']+item['goods_pic_url'][-4:])

    	i = 0
    	for each_img in item['intro_pic_urls']:
			utils.downloadImg(path,each_img,str(i)+item['goods_pic_url'][-4:])
			i = i+1


        return item
