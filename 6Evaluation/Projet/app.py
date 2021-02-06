"""
Permet l'affichage web des données scrapées
en utilisant Flask, MongoDB et ElasticSearch 
"""

from flask import Flask
from flask import request
from flask import render_template, render_template_string
from flask import flash, redirect, request, url_for

import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.graph_objs as go
import json
import re
import numpy as np
from bar import SearchBar

# from bokeh.embed import json_item
# from bokeh.models import (HoverTool, FactorRange, Plot, LinearAxis, Grid, Range1d)
# from bokeh.models.glyphs import VBar
# from bokeh.plotting import figure
# from bokeh.embed import components
# from bokeh.models.sources import ColumnDataSource
# from bokeh.resources import CDN
# from jinja2 import Template
# from bokeh.io import show, output_file
import os
from pymongo import MongoClient
# from search_bar import SearchBar
# #from graphs import create_bargraph

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

LOCAL = True
Bilboard_ES = Elasticsearch(hosts=["localhost" if LOCAL else "elasticsearch"])
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'



@app.route('/')
def rien():
  return redirect('/MusicbarLooker')



@app.route('/MusicbarLooker', methods=('GET', 'POST'))
def MusicSearch():
    """
    Création de la barre de recherche ainsi que de l'affichage des données, et affichage du bargraph
    """
    form = SearchBar()
    if form.validate_on_submit():
        return redirect('/MusicSearchSinger/'+form.typing.data)
    return render_template('search.html',form=form)

def generate_data(documents):
    """
    Génération des données cherchées
    """
    for docu in documents:
        yield {
            "_index": "lyrics",
            "_type": "lyrics",
            "_source": {k:v if v else None for k,v in docu.items()},
        }

@app.route('/MusicSearchSinger/<search_word>', methods=('GET', 'POST'))       
def search_singer(search_word):
    path = os.getcwd()+ r"\6Evaluation"+"\Projet"+r"\billboard\billboard"+"\lien.csv"
    data = pd.read_csv(path)
    documents = data.fillna("").to_dict(orient="records")
    bulk(Bilboard_ES, generate_data(documents))
    
    
    
    singer_name = str(search_word).lower()
    QUERY = {
      "query": {
        "match" : { 
            "artist" : singer_name,
            } 
      }
    }
    result = Bilboard_ES.search(index="lyrics", body=QUERY)
    source = result["hits"]["hits"]
    seen = set()
    new_source = []
    for d in source:
        t = tuple(d["_source"].items())
        if t not in seen:
            seen.add(t)
            new_source.append(d)
    
    artist = [elt['_source']['artist'] for elt in new_source]
    title = [elt['_source']['title'] for elt in new_source]
    # test = [elt['_source']['title'] for elt in result["hits"]["hits"]]
    return render_template('results.html',title=title,artists=artist)

@app.route('/MusicSearchTitle', methods=('GET', 'POST'))
def search_title(title):
    title_name = str(title).lower() + "~"
    QUERY = {
      "query": {
        "term" : { 
            "title" : title_name,
            } 
      }
    }
    result = Bilboard_ES.search(index="lyrics", body=QUERY)
    return [elt['_source']['title'] for elt in result["hits"]["hits"]]

@app.route('/MusicSearchLyrics', methods=('GET', 'POST'))
def search_lyrics(lyrics):
    lyrics_name = str(lyrics).lower() + "~"
    QUERY = {
      "query": {
        "term" : { 
            "lyrics" : lyrics_name,
            } 
      }
    }
    result = Bilboard_ES.search(index="lyrics", body=QUERY)
    return [elt['_source']['title'] for elt in result["hits"]["hits"]]

if __name__ == '__main__':
    print("Running...")
    app.run(debug=True, port=2746)