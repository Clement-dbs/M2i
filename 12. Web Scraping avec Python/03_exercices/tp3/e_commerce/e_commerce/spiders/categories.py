import scrapy
from e_commerce.items import CategoriesItem
from e_commerce.spiders import CategoriesSpider



class CategoriesSpider(scrapy.Spider):
    name = "categories"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com"]

    def parse(self, response):
        categories = response.css(".side_categories ul li ul li a")

        for category in categories:
            item = CategoriesItem()
            item['text'] = category.css("::text").get().strip()
            item['url'] = category.css("::attr(href)").get()

            yield item
        next_page = item['url']
        if next_page:
            yield response.follow(next_page, callback=CategoriesSpider.parse())

# commande pour lancer ce spider
# scrapy crawl quotes_items => infos dans le terminal
# scrapy crawl quotes_items -O outputs/quotes_items.json