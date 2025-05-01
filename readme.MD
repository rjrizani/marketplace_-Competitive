
cd marketplace
scrapy crawl firstcry
scrapy crawl snooplay

scrapy shell
fetch("https://snooplay.in/products/plot-4-balls-active-play-game-for-kids")

scrapy crawl snooplay -o snooplay.csv

scrapy crawl firstcry -o output.json
scrapy crawl firstcry -o firstcry.json
