import re
import scrapy
import numpy as np
import pandas as pd

dfGoogle = pd.read_csv("D:/GITHUB/BillboardGP/6Evaluation/Projet/billboard/billboard/dataGoogle.csv")
i = 0

class GoogleSpider(scrapy.Spider):
    name = 'google'
    allowed_domains = ['google.fr']
    start_urls = ['https://google.fr/search?q='+str('genius')+"+"+str(dfGoogle['artist'][i])+"+"+str(dfGoogle['title'][i])]

    def parseGoogle(self, response):
        global i

        lienBrut = response.css('a::attr(href)')[18].extract()
        yield {
            'lien' : re.findall(r"(?<=https){2}(.*)(?=lyrics)", lienBrut)
        }

        i = i + 1
        next_song_string = "genius+"+str(dfGoogle['artist'][i])+"+"+str(dfGoogle['title'][i])
        next_page_url = f'https://google.fr/search?q={next_song_string}'

        yield scrapy.Request(next_page_url, callback=self.parse)

    # def parseGenius(self, response):
    #     lyricsBrut = response.css('div.Lyrics__Container-sc-1ynbvzw-2.jgQsqn').get()
    #     lyricsClean = re.sub(r"<.*?>"," ", lyricsBrut)

    #     for hit in lyricsBrut:
    #         yield {
    #             'title': dfGoogle['title'][i],
    #             'artist': dfGoogle['artist'][i],
    #             'lyrics': lyricsClean
    #         }

    #     i = i + 1
    #     next_song_string = +str(genius)+"+"+str(dfGoogle['artist'][i])+"+"+str(dfGoogle['title'][i])
    #     next_page_url = f'https://google.fr/search?q={next_song_string}'
    #     yield scrapy.Request(next_page_url, callback=self.parseGoogle)
