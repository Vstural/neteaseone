import scrapy

import re

class easeSpider(scrapy.Spider):
	name = "ease"
	allowed_domains = [
	"1.163.com",
	]
	start_urls = [
	"http://1.163.com/list.html",
	# "http://1.163.com/detail/148.html"
	]

	def parse(self,respones):
		for sel in respones.xpath('//*[@id="goodsList"]/li'):
			next_url = sel.xpath('div/p/a/@href').extract()[0]
			re_digital = re.compile(r"\d+")
			file_id = re_digital.findall(next_url)[0]

			item_name = sel.xpath('div/p/a/@title').extract()[0]			
			# images = sel.xpath('div/p/a/@title').extract()

			'''
		    request = scrapy.Request("http://www.example.com/some_page.html",
                         callback=self.parse_page2)
   			request.meta['item'] = item
			'''
			# respones.meta()
			intro = ""
			print(file_id)
			 # request = scrapy.Request("http://www.example.com/some_page.html",
    #                          callback=self.parse_page2)
			# yield scrapy.Request(next_url,callback=parse_intro)

	def parse_intro(self,respones):
		pass