import re
from scrapy import Spider

from crawlers.items import Movie

def get_text(raw):
    TAG_RE = re.compile(r'<[^>]+>')

    return re.sub(TAG_RE, '', raw)

def get_text_from_list(rawList):
    str = ''

    for raw in rawList:
        str += get_text(raw)

    return str

class WikiMovieSpider(Spider):
    name = 'wiki_spider'
    start_urls = [
        'https://bg.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%91%D1%8A%D0%BB%D0%B3%D0%B0%D1%80%D1%81%D0%BA%D0%B8_%D1%84%D0%B8%D0%BB%D0%BC%D0%B8',
        'https://bg.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%91%D1%8A%D0%BB%D0%B3%D0%B0%D1%80%D1%81%D0%BA%D0%B8_%D1%84%D0%B8%D0%BB%D0%BC%D0%B8&pagefrom=%D0%95%D1%81%D0%B5%D0%BD%D0%BD%D0%BE+%D1%81%D0%BB%D1%8A%D0%BD%D1%86%D0%B5',
        'https://bg.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%91%D1%8A%D0%BB%D0%B3%D0%B0%D1%80%D1%81%D0%BA%D0%B8_%D1%84%D0%B8%D0%BB%D0%BC%D0%B8&pagefrom=%D0%9D%D0%B0%D0%B1%D0%BB%D1%8E%D0%B4%D0%B0%D1%82%D0%B5%D0%BB%D1%8F',
        'https://bg.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%91%D1%8A%D0%BB%D0%B3%D0%B0%D1%80%D1%81%D0%BA%D0%B8_%D1%84%D0%B8%D0%BB%D0%BC%D0%B8&pagefrom=%D0%A1%D0%BA%D0%BE%D1%80%D0%BF%D0%B8%D0%BE%D0%BD+%D1%81%D1%80%D0%B5%D1%89%D1%83+%D0%94%D1%8A%D0%B3%D0%B0',
    ]

    def parse(self, response):
        for movies in response.css('#mw-pages .mw-category .mw-category-group'):
            for movie_page in movies.css('ul > li'):
                yield response.follow(movie_page.css('a::attr(href)').get(), self.movie_info)
    
    def movie_info(self, response):
        movie = Movie()

        movie['title'] =  response.css('#firstHeading .mw-page-title-main::text').get()
        movie['description'] = get_text_from_list(response.css('#content #mw-content-text .mw-parser-output > p').getall())
        movie['director'] = response.css('.mw-parser-output .infobox tbody tr:nth-of-type(2) td > a::text').get()
        movie['writter'] = response.css('.mw-parser-output .infobox tbody tr:nth-of-type(3) td > a::text').get()
        movie['operator'] = response.css('.mw-parser-output .infobox tbody tr:nth-of-type(6) td > a::text').get()

        # TODO 
        # Actors

        yield movie