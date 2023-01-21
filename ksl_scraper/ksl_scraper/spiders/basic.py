import scrapy
from ksl_scraper.items import KslBlog

from datetime import datetime

make_datetime = lambda yr, m, d: datetime(year=yr, month=m, day=d).strftime('%Y/%m/%d')
make_url = lambda yr, m, d: f"https://www.ksl.com/archive/{make_datetime(yr, m, d)}/_"

def ksl_urls(yr, m_name):
    months = [
        {
        'name': 'December',
        'number': 12,
        'num_days': 31
        },
        {
        'name': 'January',
        'number': 1,
        'num_days': 31
        }
    ]

    month = [m for m in months if m['name'] == m_name][0]
    urls = [make_url(yr, month['number'], i) for i in range(1, month['num_days'] + 1)]
    return urls

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['ksl.com']
    
    def start_requests(self):
        urls = ksl_urls(2022, 'December')
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
