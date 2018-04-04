#from .base_spider import BaseSpider
import re
import json
import scrapy.crawler as crawler
from scrapy.crawler import CrawlerProcess
from multiprocessing import Process, Queue
from twisted.internet import reactor
import scrapy
import json
# import pkgutil
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

class BaseSpider(scrapy.Spider):
    def start_requests(self):
        products = {
            "nintendoswitch": ["https://www.amazon.co.jp/gp/product/B01N5QLLT3/ref=s9u_simh_gw_i1?ie=UTF8&pd_rd_i=B01NCXFWIZ&pd_rd_r=6750bbb5-37e6-11e8-b048-5d3ff3a29bf4&pd_rd_w=5Cm67&pd_rd_wg=lCmJm&pf_rd_m=AN1VRQENFRJN5&pf_rd_s=&pf_rd_r=J5NZPTYA1MZG2RZDEQF8&pf_rd_t=36701&pf_rd_p=d4802771-73ad-49b1-a154-90aaec384d3e&pf_rd_i=desktop&th=1"]    
                
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
                            


class AmazonSpider(BaseSpider):
    name = "amazon.co.jp"

    def parse(self, response):
        item = response.meta.get('item',{})
        item['url'] = response.url
        item['title'] = response.css("span#productTitle::text").extract_first().strip()
        item['price'] = float(
            ''.join(re.findall("\d+", response.css("span#priceblock_ourprice::text").extract_first()))
            )
        #yield item
        with open('results.json', 'a') as f:
            json.dump(item, f)
            f.write('\n')

        EMAIL_HOST = 'email-smtp.us-west-2.amazonaws.com'
        EMAIL_HOST_USER = 'AKIAJMYOJ25C2GK3R2HQ'
        EMAIL_HOST_PASSWORD = 'Au3LGtXGMNyVpXOdlO31XyiFusnKXiWEzNk1H0Abu15K'
        EMAIL_PORT = 587
        
        product = item['product_name']
        price = item['price']
        url = item['url']
        if price < 30000:
            msg = MIMEText("Hi!\nA good price {0}yen of {2} has been found.\nBuy the product at {1}\nHave fun!".format(price,url,product))

            me = 'yan39123@gmail.com'
            you = 'yan39123@gmail.com'

            msg['Subject'] = '[AmazonSpider] A good price has been found.'
            msg['From'] = me
            msg['To'] = you

            s = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
            s.starttls()
            s.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            s.sendmail(me, you, msg.as_string())
            s.quit()




"""

def run_spider():
    def f(q):
        try:
            runner = crawler.CrawlerRunner()
            deferred = runner.crawl(AmazonSpider)
            deferred.addBoth(lambda _: reactor.stop())
            reactor.run()
            q.put(None)
        except Exception as e:
            q.put(e)

    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    result = q.get()
    p.join()

    if result is not None:
        raise result


run_spider()
"""
