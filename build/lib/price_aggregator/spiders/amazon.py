from .base_spider import BaseSpider
import re

class AmazonSpider(BaseSpider):
    name = "amazon.co.jp"

    def parse(self, response):
        item = response.meta.get('item',{})
        item['url'] = response.url
        item['title'] = response.css("span#productTitle::text").extract_first().strip()
        item['price'] = float(
            ''.join(re.findall("\d+", response.css("span#priceblock_ourprice::text").extract_first()))
            )
        yield item
        
