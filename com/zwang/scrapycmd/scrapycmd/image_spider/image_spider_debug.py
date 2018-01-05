# -*-coding:utf-8 -*-
# 通过调用命令行进行调试

__author__ = "zwang"
__date__ = "2017/9/27"
import os
import sys

from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "image_spider", "-o", "items.json"])
# execute(["scrapy", "crawl", "image_spider"])
