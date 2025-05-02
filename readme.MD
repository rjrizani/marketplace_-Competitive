
cd marketplace
scrapy crawl firstcry
scrapy crawl snooplay

scrapy shell
fetch("https://snooplay.in/products/plot-4-balls-active-play-game-for-kids")

scrapy crawl snooplay -o snooplay.csv

scrapy crawl firstcry -o output.json
scrapy crawl firstcry -o firstcry.json

Discounts on the FirstCry marketplace typically range from 40% to 60%, while discounts on the Snooplay marketplace are more variable, ranging from 10% to 60% depending on the product.