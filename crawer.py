import requests
import scrapy
import pymongo
from bs4 import BeautifulSoup
from random import seed
from scrapy import Request, Selector
import re
from urllib import request
from urllib.request import Request, urlopen

MONGO_CLIENT = pymongo.MongoClient("mongodb://localhost:27017/")

DB = MONGO_CLIENT["fmi-project"]

movies = DB["movies"]


def full_inner_page_url(part, url_list=None):
    if url_list is None:
        url_list = []
    for part_url in part:
        url_list.append("http://www.imdb.com" + part_url)
    return url_list


def get_anything_you_want(part_url_list):
    for url in full_inner_page_url(part_url_list):
        session_obj = requests.Session()
        response = session_obj.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.content, 'html.parser')
        for i in soup.find_all(class_="sc-16ede01-1 kgphFu"):
            print(i.text)
    #class_="sc-16ede01-1 kgphFu" this is css class for short description


class MovieSpider(scrapy.Spider):
    name = 'imdb_top_movies'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/']

    def parse(self, response):
        global part_url_list
        for title in response.css('.lister-list .titleColumn a'):
            movie = {
                'title': title.css('::text').get()
            }
            movies.insert_one(movie)

            part_url_list = response.css('.lister-list .titleColumn a ::attr(href)').extract()

            yield movie
        get_anything_you_want(part_url_list)
