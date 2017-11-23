# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JianshuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author = scrapy.Field()
    title = scrapy.Field()
    pulish_time = scrapy.Field()
    abstract = scrapy.Field()
    read_number = scrapy.Field()
    comment_number = scrapy.Field()
    collect_number = scrapy.Field()
    item_url = scrapy.Field()