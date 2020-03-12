# -*- coding: utf-8 -*-
import scrapy


class KhabibSpider(scrapy.Spider):
    name = 'khabib'
    allowed_domains = ['brainyquote.com']
    start_urls = ['http://brainyquote.com/authors/khabib-nurmagomedov-quotes/']

    def parse(self, response):
        info = response.xpath('.//*[@class = "clearfix"]')

        for number in info:
            quote = number.xpath('.//a/text()').extract()
            yield {
                'quote'  : quote
            }
