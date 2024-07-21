# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ChitarachayascraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ItemDetails(scrapy.Item):
    category = scrapy.Field()
    name = scrapy.Field()
    no_of_reviews = scrapy.Field()
    rating = scrapy.Field()        
    delivery_time = scrapy.Field()
    price = scrapy.Field()
