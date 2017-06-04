import scrapy

from demo.items import OpenLabItem

class OpenLabsSpider(scrapy.Spider):
    name = "images"
    allowed_domains = [""]

    start_urls = ["http://www.openlabs.mx/"]

    def parse(self, response):
        images = response.css('img::attr("src")').extract()
	for img in images:
	        item = OpenLabItem()
	        item['file_urls'] = [img]
	        yield item
