# -*- coding: utf-8 -*-
import scrapy
import json
import urlparse
from linkfinder.items import LinkfinderItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exporters import JsonLinesItemExporter

class LinksSpider(CrawlSpider):
    name = "links"
    # allowed_domains = ['curioustails.com']
    start_urls = ['http://phoenix.craigslist.org/']

    # rules = [
    #     # Extract links matching 'category.php' (but not matching 'subsection.php')
    #     # and follow links from them (since no callback means follow=True by default).
    #     Rule(LinkExtractor(deny=r'forums*' ), follow=True),
    #
    #     # Extract links matching 'item.php' and parse them with the spider's method parse_item
    #     # Rule(LinkExtractor(allow=('https://', ))),
    # ]

    def parse(self, response):

        for link in response.xpath(".//a"):
            item = LinkfinderItem()
            yield {
                'site_title': link.xpath('//title/text()').extract(),
                'anchor_text': link.css('a::text').extract(),
                'link': urlparse.urljoin(response.url, link.css('a::attr(href)').extract_first()),
            }

        next_link = link.css('a::attr(href)').extract_first()
        if next_link is not None:
            next_link = response.urljoin(next_link)
            yield scrapy.Request(next_link, callback=self.parse)
