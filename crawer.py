import scrapy

class BlogSpider(scrapy.Spider):
    name = 'imdb_top_movies'
    start_urls = ['https://www.imdb.com/chart/top/']

    def parse(self, response):
        for title in response.css('.lister-list .titleColumn a'):
            yield {'title': title.css('::text').get()}