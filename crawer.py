import scrapy
import pymongo

MONGO_CLIENT = pymongo.MongoClient("mongodb://localhost:27017/")

DB = MONGO_CLIENT["fmi-project"]

movies = DB["movies"]

class BlogSpider(scrapy.Spider):
    name = 'imdb_top_movies'
    start_urls = ['https://www.imdb.com/chart/top/']

    def parse(self, response):
        for title in response.css('.lister-list .titleColumn a'):
            movie = {
                'title': title.css('::text').get()
            }

            yield movies.insert_one(movie)