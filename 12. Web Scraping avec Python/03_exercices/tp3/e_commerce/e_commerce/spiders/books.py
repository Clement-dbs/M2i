import scrapy
from e_commerce.items import BooksItem

class BooksSpider(scrapy.Spider):
    name = "categories"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com"]

    def parse(self, response):
        categories = response.css("product_pod")

        for category in categories:
            item = BooksItem()
            item['text'] = category.css("h3 a::attr(title)").get()
        

            yield item

# commande pour lancer ce spider
# scrapy crawl quotes_items => infos dans le terminal
# scrapy crawl quotes_items -O outputs/quotes_items.json