import scrapy
from chatScrapper.items import ChatScrapperItem

class MySpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['example.com']
    start_urls = ['https://en.wikipedia.org/wiki/National_Institute_of_Technology,_Silchar']

    def parse(self, response):
        for article in response.css('article'):
            item = ChatScrapperItem()
            item['title'] = article.css('h2 a::text').get()
            item['link'] = article.css('h2 a::attr(href)').get()
            yield item
