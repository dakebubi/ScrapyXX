# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector

from scrapycmd.items import MyImagesItem


class MyImageSpider(scrapy.Spider):
    name = "image_spider"
    allowed_domains = ["http://www.importnew.com/"]
    start_urls = [
        "http://www.importnew.com/",
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        imgs = hxs.select('//img/@src').extract()
        item = MyImagesItem()
        item['image_urls'] = imgs
        return item
