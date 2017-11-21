import scrapy
class TestSpider(scrapy.spiders.Spider):
    name = 'test'
    allowed_domains = ["www.resource-zone.com"]
    start_urls = [
        "https://www.resource-zone.com/forum/t/39973/"
    ]
    def parse(self, response):
        filename = response.url.split("/")[-2]+'.txt'
        with open(filename, 'wb') as f:
            f.write(response.body)
