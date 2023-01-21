# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KslBlog(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    url = scrapy.Field()
    date_posted = scrapy.Field()
    date_posted = scrapy.Field()
    excerpt = scrapy.Field()
    
