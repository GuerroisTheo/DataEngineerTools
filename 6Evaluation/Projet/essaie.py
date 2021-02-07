from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

dfTitreArtist = pd.read_csv("C:/Users/Theo/Documents/GITHUB/BillboardGP/6Evaluation/Projet/billboard/billboard/dataGoogle3.csv")
dfGenius = pd.read_csv("C:/Users/Theo/Documents/GITHUB/BillboardGP/6Evaluation/Projet/billboard/billboard/dataGoogle2.csv")

start_urls = []

final = pd.DataFrame()
for j in range(len(dfGenius['artist'])):
    start_urls.append('https://genius.com/'+str(dfGenius['artist'][j])+"-"+str(dfGenius['title'][j])+"-lyrics")

dicfin = {}
for i in range(len(start_urls)):
    try:
        page = requests.get(start_urls[i])
        html = BeautifulSoup(page.content, 'lxml')
        dicfin[str(dfGenius['title'][i])] = {'artist': str(dfGenius['artist'][i]), 'lyrics' : html.find("div", class_="lyrics").get_text()}
    except:
        pass

final = pd.from_dict(dicfin,orient='index')


final.to_csv('lienfinal.csv')