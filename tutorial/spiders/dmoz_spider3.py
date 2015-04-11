import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from tutorial.items import DmozItem

class DmozSpider(CrawlSpider):
    name = "dmoz3"
    allowed_domains = ["dmoz.org"]
    start_urls = ["http://www.dmoz.org/Computers/Programming/Languages"]

    rules = (
        Rule(LinkExtractor(allow=('Languages', )), callback='parse_item'),)

    def parse_item(self, response):
        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
