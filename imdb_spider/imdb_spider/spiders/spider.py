from scrapy import Spider
from datetime import datetime

from elasticsearch import Elasticsearch

ELASTIC_PASSWORD = 'RRfdxagvI1HKL9l+5Pd1'
ELASTIC_FINGERPRINT = '34752822c2815921bc7f159894d82546ad4e076b0da60561a2269d018061f703'

es = Elasticsearch(
    "https://localhost:9200",
    ssl_assert_fingerprint = ELASTIC_FINGERPRINT,
    basic_auth = (
        "elastic", 
        ELASTIC_PASSWORD
    )
)

class MovieSpider(Spider):
    name = 'imdb_movies'
    start_urls = ['https://www.imdb.com/chart/top']

    def parse(self, response):
        for movie_page in response.css('.lister-list .titleColumn'):
            yield response.follow(movie_page.css('a::attr(href)').get(), self.movie_info)

    def movie_info(self, response):
        movie_doc = {
            'title': response.css("section.ipc-page-section > div.sc-80d4314-0 h1.sc-b73cd867-0::text").get(),
            'rating': response.css('div.ipc-button__text > div.sc-f6306ea-3 > div.sc-7ab21ed2-0 span.sc-7ab21ed2-1::text').get(),
            'intro': response.css('p.sc-16ede01-6 span.sc-16ede01-2::text').get(),
            'director': response.css('div.ipc-metadata-list-item__content-container > ul > li.ipc-inline-list__item > a::text').get(),
            'poster': response.css('div.ipc-poster > div.ipc-media > img.ipc-image::attr(src)').get(),
            'timestamp': datetime.now(),
        }

        """    
            TODO
            CAST
            WRITERS
            TAGS
            Did you know
            Production company
            RELEASE YEAR
            genre
            story
            keywords
        """

        print(es.index(index='movies', document=movie_doc))
    
        yield movie_doc