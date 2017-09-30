#!/usr/bin/python
# -*- coding: UTF-8 -*-

from scrapy import cmdline
from spiders import zolSpider

cmdline.execute("scrapy crawl ODSpider".split())
