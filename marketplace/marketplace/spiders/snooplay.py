import scrapy
from ..items import snooplayItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SnooplaySpider(CrawlSpider):
    name = "snooplay"
    allowed_domains = ["snooplay.in"]
    start_urls = ["https://snooplay.in/collections/sale"]
    #start_urls = ["https://snooplay.in/products/plot-4-balls-active-play-game-for-kids"]

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
            link_extractor=LinkExtractor(allow=[r"/products/",
                                               r"/collections/sale", 
                                               r"p=",
                                               r"/collections/.*"
                                               
                                               ]),
                                         
                                    
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
        title = response.css("h1.product-single__title::text").get()
        if not title:
            self.logger.warning(f"Title not found for URL: {response.url}")
            return
        
        product_price = response.css("span.product__price::text").get()
        original_price = response.css("span.product__price.product__price--compare::text").get()
        price_w_discount = response.css("p.extra_disc::text").get()


        item = snooplayItem()
        item["title"] = title.strip() if title else None
        item["product_price"] = product_price if product_price else None
        item["original_price"] = original_price if original_price else None
        item["price_w_discount"] = price_w_discount if price_w_discount else None
        item['url'] = response.url if response.url else None # Make sure response.url exists

        yield item
      
