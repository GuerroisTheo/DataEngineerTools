from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import numpy as np
import pandas as pd
import json

df_bilboard = pd.read_csv("lien.csv")

LOCAL = True

Bilboard_ES = Elasticsearch(hosts=["localhost" if LOCAL else "elasticsearch"])


def generate_data(documents):
    for docu in documents:
        yield {
            "_index": "movies",
            "_type": "movie",
            "_source": {k:v if v else None for k,v in docu.items()},
        } 

document = df_bilboard.fillna("").to_dict(orient="records")
bulk(Bilboard_ES, generate_data(document))



def search_singer(singer):
    QUERY = {
      "query": {
        "term" : { 
            "artist" : singer.lower()} 
      }
    }
    result = Bilboard_ES.search(index="nom_du_nouveau_index", body=QUERY)
    print(result)
    return [elt['_source']['title'] for elt in result["hits"]["hits"]]

def search_title(title):
    QUERY = {
      "query": {
        "term" : { 
            "title" : title.lower()} 
      }
    }
    result = Bilboard_ES.search(index="nom_du_nouveau_index", body=QUERY)
    print(result)
    return [elt['_source']['title'] for elt in result["hits"]["hits"]]

def search_lyrics(lyrics):
    QUERY = {
      "query": {
        "term" : { 
            "lyrics" : lyrics.lower()} 
      }
    }
    result = Bilboard_ES.search(index="nom_du_nouveau_index", body=QUERY)
    print(result)
    return [elt['_source']['title'] for elt in result["hits"]["hits"]]