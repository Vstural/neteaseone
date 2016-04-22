import scrapy
from ease.items import EaseItem
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
			goods_pic_url = sel.xpath('//*[@id="goodsList"]/li[1]/div/div[1]/a/img').extract()
			next_url = "http://1.163.com" + next_url
			
			item = EaseItem()
			item['file_id'] = file_id
			item['item_name'] = item_name
			item['goods_pic_url'] = goods_pic_url

			request = scrapy.Request(next_url,callback=self.parse_intro)
			request.meta['item'] = item

			yield request

	def parse_intro(self,respones):
		item = respones.meta['item']
		print item['item_name']
		# print respones.url
		yield item