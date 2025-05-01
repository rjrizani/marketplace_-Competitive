import scrapy
from ..items import firstcryItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class FirstcrySpider(CrawlSpider):
    name = "firstcry"
    allowed_domains = ["www.firstcry.com"]
    #start_urls = ["https://www.firstcry.com"]
    #start_urls = ["https://www.firstcry.com"]
    start_urls = ["https://www.firstcry.com/searchresult?sale=6&searchstring=brand@@@@1@0@20@@@@@@@@@@@@@@@@&sort=bestseller&gender=boy,unisex&ref2=menu_dd_boy-fashion_bestsellers_V#sale=6&searchstring=brand@@@@1@0@20@@@@@@@@@@@@@@@@@@@@@&rating=&sort=bestseller&&vi=three&pmonths=&cgen=&skills=&measurement=&material=&curatedcollections=&Color=&Age=&gender=both,male&ser=&premium=&deliverytype=&PageNo=1&scrollPos=0&pview=&tc=100822"]
    custom_settings = {
        "DOWNLOAD_HANDLERS": {
            "http": "scrapy_impersonate.ImpersonateDownloadHandler",
            "https": "scrapy_impersonate.ImpersonateDownloadHandler",
        },
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
    }

    def enable_impersonate(self, request, response):
        request.meta["impersonate"] = "chrome110"
        return request
   
    rules = [
        
        Rule(
   
 #           link_extractor=LinkExtractor(allow=[r"bestsellers", 
  #                                              r"NewArrivals",
   #                                          
    #                                           
     #                                          ]),
        
                                    
            follow=True,
            callback="parse_item",
            process_request="enable_impersonate",
        ),
    ]


    def start_requests(self):
        for url in self.start_urls:
            for browser in ["chrome110", "edge99", "safari15_5"]:
                self.logger.info(f"Requesting {url} with browser: {browser}")
                yield scrapy.Request(
                    url,
                    dont_filter=True,
                    meta={"impersonate": browser},
                )


    def parse_item(self, response):
        # filepath: c:\Users\rjriz\freelance\marketplace_ Competitive\marketplace\marketplace\spiders\snooplay.py
        title = response.css("a > img::attr(title)").getall()[3:-1]
        
     
        
        product_price = response.css("div.rupee.fw.lft .r1.B14_42 a::text").getall()
        original_price = response.css("span.r2.R12_42 a::text").getall()
        club_price = response.css("span.r1.B12_blue a::text").getall()
        url = response.url

        if not title or not product_price:
            self.logger.warning(f"Title or Product Price not found for URL: {response.url}")
            return
      

        print(f"Title: {title}")
        print(f"Product Price: {product_price}")
        print(f"Original Price: {original_price}")
        print(f"Club Price: {club_price}")

        item = firstcryItem()
        item['title'] = title
        item['product_price'] = product_price if product_price else None
        item['original_price'] = original_price if original_price else None
        item['club_price'] = club_price if club_price else None
        item['url'] = url

        yield item


       