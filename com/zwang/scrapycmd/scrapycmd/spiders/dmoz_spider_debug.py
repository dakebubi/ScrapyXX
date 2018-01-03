# -*-coding:utf-8 -*-
"""
通过debug模式启动爬虫，方便调试
注：回启动当前目录下所有的spider
"""
__author__ = "zwang"
__date__ = "2017/9/27"
import os
import sys

from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "dmoz", "-o", "items.json"])
