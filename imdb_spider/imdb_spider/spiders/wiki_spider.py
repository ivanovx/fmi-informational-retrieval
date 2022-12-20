from scrapy import Spider
from datetime import datetime

class WikiMovieSpider(Spider):
    name = 'wiki_spider'
    start_urls = [
        'https://bg.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%91%D1%8A%D0%BB%D0%B3%D0%B0%D1%80%D1%81%D0%BA%D0%B8_%D1%84%D0%B8%D0%BB%D0%BC%D0%B8',
        'https://bg.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%91%D1%8A%D0%BB%D0%B3%D0%B0%D1%80%D1%81%D0%BA%D0%B8_%D1%84%D0%B8%D0%BB%D0%BC%D0%B8&pagefrom=%D0%95%D1%81%D0%B5%D0%BD%D0%BD%D0%BE+%D1%81%D0%BB%D1%8A%D0%BD%D1%86%D0%B5',
        'https://bg.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%91%D1%8A%D0%BB%D0%B3%D0%B0%D1%80%D1%81%D0%BA%D0%B8_%D1%84%D0%B8%D0%BB%D0%BC%D0%B8&pagefrom=%D0%9D%D0%B0%D0%B1%D0%BB%D1%8E%D0%B4%D0%B0%D1%82%D0%B5%D0%BB%D1%8F',
        'https://bg.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%91%D1%8A%D0%BB%D0%B3%D0%B0%D1%80%D1%81%D0%BA%D0%B8_%D1%84%D0%B8%D0%BB%D0%BC%D0%B8&pagefrom=%D0%A1%D0%BA%D0%BE%D1%80%D0%BF%D0%B8%D0%BE%D0%BD+%D1%81%D1%80%D0%B5%D1%89%D1%83+%D0%94%D1%8A%D0%B3%D0%B0',
    ]

    def parse(self, response):
        for movies_info in response.css('#mw-pages .mw-category .mw-category-group'):
            for movie_page in movies_info.css('ul> li'):
                yield response.follow(movie_page.css('a::attr(href)').get(), self.movie_info)

    
    def movie_info(self, response):
        movie_doc = {
            'title': response.css('#firstHeading span.mw-page-title-main::text').get()
        }

        yield movie_doc