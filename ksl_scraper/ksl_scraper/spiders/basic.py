import scrapy
import datetime
from ksl_scraper.items import KslBlog

# https://www.ksl.com/archive/2023/01/19/_
make_url = lambda yr, m, d: f"https://www.ksl.com/archive/{yr}/{m}/{d}/"

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['ksl.com']
    #start_urls = ['https://www.ksl.com/archive/2023/01/19/_']
    
    def start_requests(self):
        urls = ['https://www.ksl.com/archive/2023/01/19/_']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        blogs = response.css('div.story.content > div.firefox_fix > div.listItem')
        for blog in blogs:
            item = KslBlog()
            item['title'] = blog.css('h1 > a::text').get()
            item['url'] = blog.css('h1 > a::attr(href)').get()
            item['date_posted'] = blog.css('div.listSub::text').get()
            item['excerpt'] = blog.xpath('self::div//text()').get()
            yield item
