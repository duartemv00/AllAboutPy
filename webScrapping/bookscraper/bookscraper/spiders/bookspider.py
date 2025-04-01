import scrapy
from bookscraper.items import BookItem

class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"] # avoid crawling other domains
    start_urls = ["https://books.toscrape.com"] # URL where the scraping starts

#======================================================================

    def parse(self, response):
        """
        Documentation
        """
        books = response.css('article.product_pod')
        
        # Loop through each book in the current page
        for book in books:
            book_page = book.css("h3 a ::attr(href)").get()
            if book_page is not None:
                if 'catalogue/' in book_page:
                    book_page_url = 'https://books.toscrape.com/' + book_page
                else:
                    book_page_url = 'https://books.toscrape.com/catalogue/' + book_page
                yield response.follow(book_page_url, callback= self.parse_book_page)

        # Get the next page URL
        next_page = response.css("li.next a ::attr(href)").get()
        if next_page is not None:
            if 'catalogue/' in next_page:
                next_page_url = 'https://books.toscrape.com/' + next_page
            else:
                next_page_url = 'https://books.toscrape.com/catalogue/' + next_page
            yield response.follow(next_page_url, callback= self.parse)

#======================================================================

    def parse_book_page(self, response):
        """
        Documentation
        """

        table_rows = response.css("table tr")
        book_item = BookItem()
        
        book_item['url'] = response.url,
        book_item['title'] = response.css('.product_main h1::text').get(),
        book_item['category'] = response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get(),
        book_item['description'] = response.xpath("//div[@id='product_description']/following-sibling::p/text()").get(),
        book_item['stars'] = response.css('p.star-rating').attrib['class'],
        book_item['price'] = response.css('.price_color ::text').get(),
        book_item['UPC'] = table_rows[0].css('td::text').get(),
        book_item['product_type'] = table_rows[1].css('td::text').get(),
        book_item['price_excl_tax'] = table_rows[2].css('td::text').get(),
        book_item['price_incl_tax'] = table_rows[3].css('td::text').get(),
        book_item['tax'] = table_rows[4].css('td::text').get(),
        book_item['availability'] = table_rows[5].css('td::text').get(),
        book_item['num_of_reviews'] = table_rows[6].css('td::text').get()

        yield book_item



"""yield {
    'url' : response.url,
    'title' : response.css('.product_main h1::text').get(),
    'category' : response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get(),
    'description' : response.xpath("//div[@id='product_description']/following-sibling::p/text()").get(),
    'stars' : response.css('p.star-rating').attrib['class'],
    'price' : response.css('.price_color ::text').get(),
    'UPC' : table_rows[0].css('td::text').get(),
    'product-type' : table_rows[1].css('td::text').get(),
    'price-excl-tax' : table_rows[2].css('td::text').get(),
    'price-incl-tax' : table_rows[3].css('td::text').get(),
    'tax' : table_rows[4].css('td::text').get(),
    'availability' : table_rows[5].css('td::text').get(),
    'num-of-reviews' : table_rows[6].css('td::text').get()
}"""