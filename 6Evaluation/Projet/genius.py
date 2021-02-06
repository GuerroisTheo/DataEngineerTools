import scrapy


class GeniusSpider(scrapy.Spider):
    name = 'genius'
    allowed_domains = ['genius.com']
    start_urls = ['http://genius.com/']

    def parse(self, response):
        pass
