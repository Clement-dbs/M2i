import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com"]
    i = 1
    rating_map = {'One':1,'Two':2,'Three':3,'Four':4,'Five':5}

    def parse(self, response):
        books = response.css("article.product_pod")
    
        for book in books:
            title = book.css("h3 a::attr(title)").get()
            price = book.css("p.price_color::text").get().split('£')[1]
            rating_class = book.css('p.star-rating').attrib['class'].split(' ')[1]
            rating = self.rating_map.get(rating_class,0)
            availability = book.css("p.instock::text").getall()[1].strip()

            yield {
                "title": title,
                "price": price,
                "rating" : rating,
                "availability": availability
            }

        next_page = response.css("li.next a::attr(href)").get()
        
        if next_page and self.i <= 3:
            self.i = self.i + 1
            yield response.follow(next_page, callback=self.parse)

