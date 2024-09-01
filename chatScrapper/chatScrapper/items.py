import scrapy

class ChatScrapperItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()

