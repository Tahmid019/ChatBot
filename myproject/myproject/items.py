import scrapy

class TextToPdfItem(scrapy.Item):
    url = scrapy.Field()
    text = scrapy.Field()
