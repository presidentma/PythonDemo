from scrapy.spider import Spider
from jianshu.items import JianshuItem

class JianshuSpider(Spider):
    name = 'jianshu'
    spider_list = []
    for num in range(1,2):
        pages = 'http://www.jianshu.com/c/V2CqjW?order_by=commented_at&page={0}'.format(num)
        spider_list.append(pages)
    start_urls = spider_list
    def parse(self, res):
        item = JianshuItem()
        articles = res.xpath('//ul[@class="note-list"]/li')
        for index,article in enumerate(articles):
            item['author'] = article.xpath('//div[@class="info"]/a[1]/text()').extract()
            print(item['author'][index])