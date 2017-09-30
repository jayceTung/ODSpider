#!/usr/bin/python
# -*- coding: UTF-8 -*-
import scrapy


class ZolItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()


