# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from nhs.items import NhsItem

class NhschoiceSpider(CrawlSpider):
    name = 'nhschoice'
    allowed_domains = ['nhs.uk']
    start_urls = ['http://www.nhs.uk/Conditions/Pages/hub.aspx']

   
    rules = (
        Rule(LinkExtractor(allow=r'conditions\/'), callback='parse_item', follow=True),
    )
    

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        li = ItemLoader(item=NhsItem(), response=response)
        li.add_xpath('title', "//div[@class='healthaz-header clear']")
        li.add_xpath('content', "//body")
        return li.load_item()
        