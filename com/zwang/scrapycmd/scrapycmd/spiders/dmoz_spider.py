# -*- coding: utf-8 -*-
import logging

import scrapy

from scrapycmd.items import ScrapycmdItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"  # 命令行运行：scrapy crawl dmoz
    allowed_domains = ["dmoz.org"]
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
