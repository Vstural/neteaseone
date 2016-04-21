import scrapy

import re

def 

class easeSpider(scrapy.Spider):
	name = "ease"
	allowed_domains = [
	"1.163.com",
	]
	start_urls = [
	"http://1.163.com/list.html",
	]

	def parse(self,respones):
		for sel in respones.xpath('//*[@id="goodsList"]/li'):
			item_name = sel.xpath('div/p/a/@title').extract()[0]
			file_id = sel.xpath('div/p/a/@href').extract()[0]

			image_url = sel.xpath('div/p/a/@title').extract()#TODO
			intro = ""
			print(type(file_id))
			