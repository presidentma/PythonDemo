from scrapy.spider import Spider
from jianshu.items import JianshuItem
import re
from jianshu.deal_funcs import DealFunction

class JianshuSpider(Spider):
    name = 'jianshu'
    spider_list = []
    for num in range(1,50):
        pages = 'http://www.jianshu.com/c/V2CqjW?order_by=commented_at&page={0}'.format(num)
        spider_list.append(pages)
    start_urls = spider_list
    def parse(self, res):
        item = JianshuItem()
        articles = res.xpath('//ul[@class="note-list"]/li')
        for index,article in enumerate(articles):
            item['author'] = article.xpath('.//div[@class="info"]/a[1]/text()').extract()[0]
            item['title'] = article.xpath('.//div[@class="content"]/a[1]/text()').extract()[0]
            item['abstract'] = article.xpath('normalize-space(.//p[@class="abstract"]/text())').extract()[0]
            pulish_time = article.xpath('.//div[@class="info"]//span/@data-shared-at').extract()[0]
            item_url = article.xpath('.//div[@class="content"]/a/@href').extract()[0]
            item['item_url'] = 'http://www.jianshu.com' + str(item_url)
            read_number = article.xpath('.//div[@class="meta"]/a[1]/text()').extract()[1]
            comment_number = article.xpath('.//div[@class="meta"]/a[2]/text()').extract()[1]
            collect_number = article.xpath('.//div[@class="meta"]/span/text()').extract()[0]
            item['pulish_time'] = DealFunction().format_time(pulish_time)
            item['comment_number'] = re.sub(r'\s+','',read_number)
            item['read_number'] = re.sub(r'\s+','',read_number)
            item['collect_number'] = re.sub(r'\s+','',collect_number)
            yield item
