import scrapy
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from lxml import html


class PycoderSpider(scrapy.Spider):
    name = "pycoder"
    allowed_domains = ["pycoders.com"]
    start_urls = [
        "http://pycoders.com/archive/"
    ]

    def start_requests(self):
        requests = list(super(MySpider, self).start_requests())
        #requests += [scrapy.Request(x, self.parse_other) for x in self.other_urls]
        return requests

    parse(self,tart_requests(self):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
        for sel in response.xpath('//div'):
            print sel
        #for sel in response.xpath('//div[@class="display_archive"]'):
        #    print sel
            #link = sel.xpath('a/@href').extract()
            #print link

