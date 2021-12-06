import scrapy
from amazon_scrapy.items import AmazonScrapyItem
import time
from scrapy.exceptions import CloseSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor



class AmazonSpider(scrapy.Spider):
    name = 'amazon_items'
    allowed_domains = ['amazon.in']

    key_word=input("item name  ")
    start_urls = ["https://www.amazon.in/s?k="+(key_word)]
    # start_urls = ["https://www.amazon.in/s?k=smart+watch&page=1&qid=1638795301&ref=sr_pg_6"]
    def parse(self,response):
        # for sel in response.xpath('//*[@class="a-section a-spacing-medium a-text-center"]'):
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
        # print("sadgrgxcwefw",i)
        # next_urls = response.css(".a-last a::attr(href)").extract_first()
        next_urls = response.xpath(".//*[@class='a-text-center']//li[@class='a-last']/a/@href").extract_first()
        urls="amazon.in"+(next_urls)
        url=response.urljoin(urls)

        print("RCTBITGVTVSJNSOHBS_>",len(url))
        print("NEXT__URL__CHECK@@-->",url)
        yield scrapy.Request(url, callback=self.parse,dont_filter=True)
