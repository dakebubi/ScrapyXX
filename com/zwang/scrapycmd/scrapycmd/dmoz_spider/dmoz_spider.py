# -*- coding: utf-8 -*-
"""
运行方式：
1、cd至当前文件同目录下
2、运行scrapy crawl dmoz -o items.json
"""
import logging

import scrapy

from scrapycmd.items import ScrapycmdItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["importnew.com"]
    start_urls = [
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        "http://www.importnew.com/"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2] + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)


        logging.warning("This is a warning")
        for sel in response.xpath('//ul/li'):
            scrapycmdItem = ScrapycmdItem();
            scrapycmdItem['title'] = sel.xpath('a/text()').extract()  # 打印的是unicode
            scrapycmdItem['link'] = sel.xpath('a/@href').extract()
            scrapycmdItem['desc'] = sel.xpath('text()').extract()
            yield scrapycmdItem
