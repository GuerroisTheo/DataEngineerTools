import re
import scrapy
import numpy as np
import pandas as pd

dfTitreArtist = pd.read_csv("D:/GITHUB/BillboardGP/6Evaluation/Projet/billboard/billboard/dataGoogle3.csv")
dfGenius = pd.read_csv("D:/GITHUB/BillboardGP/6Evaluation/Projet/billboard/billboard/dataGoogle2.csv")
i = 0

class GeniusSpider(scrapy.Spider):
    global i
    name = 'genius'
    allowed_domains = ['genius.com']
    start_urls = ['https://genius.com/'+str(dfGenius['artist'][0])+"-"+str(dfGenius['title'][0])+"-lyrics"]

    def parse(self, response):
        global i
        urls = []

        for i in range(len(dfGenius['artist'])):
            urls.append('https://genius.com/'+str(dfGenius['artist'][i])+"-"+str(dfGenius['title'][i])+"-lyrics")
        
        for url in urls:
            try: 
                yield scrapy.Request(url, callback=self.parseGenius)
            except:
                pass

    def parseGenius(self, response):

        yield {
            'artist': response.xpath('//a[@class="Link-h3isu4-0 dpVWpH SongHeader__Artist-sc-1b7aqpg-9 eTAmkN"]/text()').get(),
            'title': response.xpath('//h1[@class="SongHeader__Title-sc-1b7aqpg-7 jQiTNQ"]/text()').get(),
            'lyrics': re.sub(r"<.*?>"," ", str(response.css('div.Lyrics__Container-sc-1ynbvzw-2.jgQsqn').get()) )
        }
