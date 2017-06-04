#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy

class BooksSpider(scrapy.Spider):

    name = "books4"

    start_urls = [
            'http://books.toscrape.com/',
    ]

    def parse(self, response):
        word = getattr(self, 'word', None)
        if word is not None:
		for book in response.css('.product_pod'):
                    title = book.css('h3 a::attr(title)').extract_first()
		    if word in title:
			    yield {
				'title': title, 
				'price': book.css('.price_color::text').extract_first()[1:],
			    }

		next_page = response.css('li.next a::attr(href)').extract_first()
		if next_page is not None:
		    next_page = response.urljoin(next_page)
		    yield scrapy.Request(next_page, callback=self.parse)
