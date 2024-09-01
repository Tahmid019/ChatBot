import scrapy
from myproject.items import TextToPdfItem

class TextSpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['http://www.nits.ac.in/'] 

    def parse(self, response):
        html_content = response.body

        filename = 'raw_html.html'
        with open(filename, 'wb') as f:
            f.write(html_content)

        self.log(f'Saved file {filename}')

        
