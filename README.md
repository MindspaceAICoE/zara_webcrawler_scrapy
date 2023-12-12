# zara_webcrawler_scrapy
This is a spider (web crawler) that is built using scrapy. 
The website being crawled is Zara's best-seller section(both men's and women's). 
The scraper is built to extract the following details of the products: Title, Description, Price, Colors available(if any), Image URLs, and the Product URL. 
All of this data is stored in a JSON file.
There is an option to download all the images as well, this can be done by uncommenting the 'ITEM_PIPELINES', 'IMAGES_STORE', and 'IMAGES_URLS_FIELD' in the 'Configure item pipelines' section in the 'settings.py' file.
Additionally, there is a file called 'single_spider.py' that can be used to scrape the data of a single product. 
