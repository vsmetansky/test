from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from scrapy.http import Request

from scraper.items import AutoItem


class AutoSpider(CrawlSpider):
    name = 'auto_spider'
    allowed_domains = ('auto-store.kiev.ua',)
    start_urls = ('http://www.auto-store.kiev.ua/nubira/',)

    def __init__(self, item_num, *args, **kwargs):
        self.found_num = 0
        self.item_num = item_num
        super().__init__(*args, **kwargs)

    def parse_start_url(self, response):
        for url in response.xpath('//div[@class="name"]/a/@href').getall():
            yield Request(url, callback=self.parse_item)

    def parse_item(self, response):
        self.___check_stop()
        return AutoItem(
            price=self.__price(response),
            image=self.__image(response),
            description=self.__info(response)
        )

    def __price(self, response):
        return response.xpath('//div[@class="price"]/text()').get().strip()

    def __image(self, response):
        return response.xpath('//div[@class="image"]/a/img/@src').get()

    def __info(self, response):
        return response.xpath('//div[@id="tab-description"]/div/text()').get().strip()

    def ___check_stop(self):
        if self.__stop():
            CloseSpider()
        else:
            self.found_num += 1

    def __stop(self):
        return self.found_num >= self.item_num
