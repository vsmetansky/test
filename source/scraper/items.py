import scrapy


class AutoItem(scrapy.Item):
    price = scrapy.Field()
    image = scrapy.Field()
    description = scrapy.Field()
