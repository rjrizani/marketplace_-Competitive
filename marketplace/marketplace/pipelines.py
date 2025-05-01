# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MarketplacePipeline:
    def process_item(self, item, spider):
        return item
    
class snooperPipeline:
    def process_item(self, item, spider):
        item = dict(item)
        """
        item['product_price'] = item['product_price'].strip() if item['product_price'] else None
        item['price_w_discount'] = item['price_w_discount'].strip() if item['price_w_discount'] else None

        item['original_price'] = item['original_price'].strip() if item['original_price'] else None
        """
        item['product_price'] = self.convert_price_to_float(item['product_price'])
        item['price_w_discount'] = self.convert_price_to_float(item['price_w_discount'])

        item['original_price'] = self.convert_price_to_float(item['original_price'])
        return item
    
    import pandas as pd

    def convert_price_to_float(self,price_string):
       
        if not isinstance(price_string, str):
            return None  # or return the original value

        try:
            # Remove currency symbols, commas, and other non-numeric characters
            cleaned_price = ''.join(c for c in price_string if c.isdigit() or c == '.')

            # Convert to float
            return float(cleaned_price)
        except ValueError:
            return None  # or return the original value

class firstcryPipeline:
    def process_item(self, item, spider):
        item = dict(item)
        item['product_price'] = item['product_price']
  
        item['original_price'] = item['original_price'] if item['original_price'] else item['product_price']
        item['club_price'] = item['club_price']
        return item
