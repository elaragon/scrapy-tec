#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy

class BooksSpider(scrapy.Spider):

    name = "books1"

    start_urls = [
            'http://books.toscrape.com/catalogue/page-1.html',
            'http://books.toscrape.com/catalogue/page-2.html',
    ]

    def parse(self, response):
        filename = response.url.split("/")[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

