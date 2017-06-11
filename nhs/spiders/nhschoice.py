# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.exceptions import DropItem
from nhs.items import NhsItem

class NhschoiceSpider(CrawlSpider):
    name = 'nhschoice'
    allowed_domains = ['nhs.uk']
    start_urls = ['http://www.nhs.uk/Conditions/Pages/hub.aspx']

   
    rules = (
        Rule(LinkExtractor(allow=r'\/conditions\/', unique=True), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'\/Conditions\/', unique=True), callback='parse_item', follow=True),        

    )
    

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        hasHeader = response.xpath("//div[@class='healthaz-header clear']").extract()
        
        if hasHeader:
            li = ItemLoader(item=NhsItem(), response=response)
            li.add_value('title', hasHeader[0])
            li.add_xpath('content', "//body")
            li.add_value('url', response.url)
            return li.load_item()
        else:
            raise DropItem("No header")
        