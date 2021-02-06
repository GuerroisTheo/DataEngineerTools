import scrapy


class GoogleSpider(scrapy.Spider):
    name = 'google'
    allowed_domains = ['https://google.fr/search?q=']
    start_urls = ['https://google.fr/search?q=']

    def parse(self, response):
        pass
