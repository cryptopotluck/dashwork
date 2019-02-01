import scrapy

class BlogSpider(scrapy.Spider):
    name = 'kittySpider'
    start_urls = ['https://www.rockporthomerentals.com/category/all-rentals']

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').extract_first()}

        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)
