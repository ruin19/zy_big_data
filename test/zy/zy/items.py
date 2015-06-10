# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    garden_name = scrapy.Field()
    garden_price = scrapy.Field()
    trade_date = scrapy.Field()
    garden_sumPrice = scrapy.Field()
    garden_detial = scrapy.Field()
    garden_area = scrapy.Field()
    garden_location = scrapy.Field()
    pass
