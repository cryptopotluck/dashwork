import scrapy

class KittySpider(scrapy.Spider):
    name= 'KittySpider'

    start_urls = [
        'https://www.rockporthomerentals.com/category/all-rentals'
    ]

    def parse(self, response):
        for rentals in response.xpath("//div[@class='property-list-items-wrapper']"):
            yield {
                'property_name':rentals.xpath(".//div[@class='property-list-items-wrapper']")
            }

        nex_page = response.xpath("//li[@class='next']/a/@href").extract_first()
        if nex_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)