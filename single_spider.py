import scrapy

class ZaraSpider(scrapy.Spider):
    name = "single_spider"

    start_urls = ["https://www.zara.com/in/en/contrast-printed-t-shirt-p03665315.html?v1=283383871&v2=2297854",]

    # def parse(self, response):
    #     # Extract product URLs from the product listing page
    #     product_urls = response.css("a.product-link::attr(href)").getall()

    #     # Pass the product URLs to the ZaraSpider
    #     for product_url in product_urls:
    #         yield scrapy.Request(product_url, callback=self.parse_product_page)

    
    def parse(self, response):
        # Extracting product details
        product_title = response.css("h1.product-detail-info__header-name::text").get()
        product_current_price = response.css("span.price-current__amount span::text").get()
        product_old_price = response.css("span.price-old__amount span::text").get()
        product_discount = response.css("span.price-current__discount-percentage::text").getall()
        product_description = response.css("div.expandable-text__inner-content p::text").get()
        product_colors = response.css("div.product-detail-color-selector__color-area::attr(style)").getall()
        product_images = response.css("ul.product-detail-images__images li source::attr(srcset)").getall()

        product_colors = list({product_color.split(":")[1] for product_color in product_colors})
        product_images = list({product_image.split(" ")[0] for product_image in product_images})
        product_discount = "".join(product_discount)

        # Creating a dictionary to store the data
        product_data = {
            "Title": product_title,
            "Current_Price": product_current_price,
            "Old_Price": product_old_price,
            "Discount": product_discount,
            "Description": product_description,
            "Colors": product_colors,
            "Images": product_images,
            "URL": response.url,
        }

        # Yielding the data
        yield product_data
