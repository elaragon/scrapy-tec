#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy

class BooksSpider(scrapy.Spider):

    name = "books2"

    start_urls = [
            'http://books.toscrape.com/catalogue/page-1.html',
            'http://books.toscrape.com/catalogue/page-2.html',
    ]


    def parse(self, response):
        for book in response.css('.product_pod'):
            yield {
                'title': book.css('h3 a::attr(title)').extract_first(), 
                'price': book.css('.price_color::text').extract_first()[1:],
            }

