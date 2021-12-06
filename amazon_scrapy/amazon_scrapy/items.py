# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    brand = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    total_review = scrapy.Field()
    image_url=scrapy.Field()
    pass
