# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import item, Field

class LinkfinderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    site_title = scrapy.Field()
    anchor_text = scrapy.Field()
    link = scrapy.Field()
    pass
    
