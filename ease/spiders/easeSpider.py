import scrapy

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
			name = sel.xpath('div/p/a/@title').extract()
			print(chr(name[0]))
			