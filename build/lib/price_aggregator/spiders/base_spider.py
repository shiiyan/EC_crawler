import scrapy
import json
# import pkgutil
from datetime import datetime


class BaseSpider(scrapy.Spider):
    def start_requests(self):
        products = {
            "nintendoswitch": ["https://www.amazon.co.jp/Nintendo-Switch-Joy-%E3%83%8D%E3%82%AA%E3%83%B3%E3%83%96%E3%83%AB%E3%83%BC-%E3%83%8D%E3%82%AA%E3%83%B3%E3%83%AC%E3%83%83%E3%83%89/dp/B01NCXFWIZ/ref=sr_1_3?s=videogames&ie=UTF8&qid=1522227038&sr=1-3&keywords=switch"]
            }
        for name, urls in products.items():
            for url in urls:
                if self.name in url:
                    now = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
                    item = {'product_name':name,
                            'retailer':self.name,
                            'when': now
                            }
                    yield scrapy.Request(url, meta={'item':item})
                            
