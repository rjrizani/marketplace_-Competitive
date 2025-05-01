# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MarketplaceItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class snooplayItem(scrapy.Item):
    title = scrapy.Field()
    product_price = scrapy.Field()
    original_price = scrapy.Field()
    price_w_discount = scrapy.Field()
    url = scrapy.Field()

class firstcryItem(scrapy.Item):
    title = scrapy.Field()
    product_price = scrapy.Field()
    original_price = scrapy.Field()
    club_price = scrapy.Field()
    url = scrapy.Field()