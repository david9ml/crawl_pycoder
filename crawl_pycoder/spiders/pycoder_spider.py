import scrapy

class PycoderSpider(scrapy.Spider):
    name = "pycoder"
    allowed_domains = ["pycoders.com"]
    start_urls = [
        "http://pycoders.com/archive/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
        for sel in response.xpath('//div'):
            print sel
        #for sel in response.xpath('//div[@class="display_archive"]'):
        #    print sel
            #link = sel.xpath('a/@href').extract()
            #print link

