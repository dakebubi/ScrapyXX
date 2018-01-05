# -*- coding: utf-8 -*-
"""
运行方式：
1、cd至当前文件同目录下
2、运行scrapy crawl image_spider -o items.json
2、运行scrapy crawl image_spider -o 直接下载图片，存储路径由settings.py的IMAGES_STORE指定
"""
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
