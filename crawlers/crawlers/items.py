# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class Movie(Item):
    title = Field()
    description = Field()
    director = Field()
    writter = Field()
    operator = Field()