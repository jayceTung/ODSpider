#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

import os
import urllib
from urllib2 import Request

import scrapy
import sys
from scrapy import Selector

from ODSpider.item.zolitems import ZolItem


class ZolSpider(scrapy.spiders.Spider):
    def __init__(self):
        pass

    name = "ODSpider"

    allowed_domains = ["desk.zol.com.cn"]  # 搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页

    start_urls = ["http://desk.zol.com.cn/fengjing/1920x1080/1.html"]

    def parse(self, response):
        se = Selector(response)

        if re.match("http://desk.zol.com.cn/fengjing/\d+x\d+/\d+.html", response.url):
            src = se.xpath("//ul[@class='pic-list2  clearfix']/li")

            for i in range(len(src)):
                img_url = se.xpath("//ul[@class='pic-list2  clearfix']/li[%d]/a/img/@src"%i).extract()
                titles = se.xpath("//ul[@class='pic-list2  clearfix']/li[%d]/a/img/@title"%i).extract()

                if img_url:
                    real_url = img_url[0].replace("t_s208x130c5","t_s2560x1600c5")
                    file_name = u"%s.jpg" % titles[0]  # 要保存文件的命名

                    path = os.path.join("F:\logs", file_name)  # 拼接这个图片的路径，我是放在F盘的pics文件夹下
                    type = sys.getfilesystemencoding()
                    print file_name.encode(type)

                    item = ZolItem()  # 实例item（具体定义的item类）,将要保存的值放到事先声明的item属性中
                    item['name'] = file_name
                    item['url'] = real_url
                    print item["name"], item["url"]

                    yield item  # 返回item,这时会自定解析item

                    urllib.urlretrieve(real_url, path)

                all_urls = se.xpath("//a/@href").extract()  # 提取界面所有的url
                for url in all_urls:
                    if url.startswith("/fengjing/1920x1080/"):  # 若是满足定义的条件，继续爬取
                        yield Request("http://desk.zol.com.cn" + url, callback=self.parse)
