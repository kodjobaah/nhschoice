# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose
from w3lib.html import remove_tags

class NhsItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Join(),
    )
    content = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Join(),
   )
