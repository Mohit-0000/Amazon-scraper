import scrapy
from amazon_scrapy.items import AmazonScrapyItem
import time
from scrapy.exceptions import CloseSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor



class AmazonSpider(scrapy.Spider):
    name = 'amazon_items'
    allowed_domains = ['amazon.in']
    page=2
    next_urls_int=0
    key_word=input("Product name -  ")
    start_urls = ["https://www.amazon.in/s?k="+(key_word)]
    numbers=0
    def parse(self,response):
        for sel in response.css(".s-widget-spacing-small"):
            item = AmazonScrapyItem()
            try:
                item['title'] = sel.xpath(".//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']//span//text()").get()
            except:
                item['title'] = sel.xpath('.//*[@class="a-size-medium a-color-base a-text-normal"]//text()').get()
            item['price'] = sel.css('.a-price-whole::text').extract_first()
            item['rating'] = sel.xpath('.//*[contains(concat( " ", @class, " " ), concat( " ", "aok-align-bottom", " " ))]//text()').extract_first()
            item['total_review'] = sel.xpath('.//*[@class="a-row a-size-small"]//a/span/text()').extract_first()
            item['image_url'] = sel.css('img.s-image::attr(src)').extract_first()
            yield item
        next_test = response.xpath(".//*[@class='a-text-center']//li[@class='a-disabled']/text()").extract()
        if AmazonSpider.numbers<1:
            AmazonSpider.next_urls_int=next_test[-1]
            AmazonSpider.numbers+=1
        else:
            pass
        if AmazonSpider.page<=int(AmazonSpider.next_urls_int):
            next_urls=AmazonSpider.start_urls[0]+"&page="+str(AmazonSpider.page)
            yield scrapy.Request(next_urls, callback=self.parse,)
            AmazonSpider.page+=1
        else:
            raise CloseSpider('DONE')
