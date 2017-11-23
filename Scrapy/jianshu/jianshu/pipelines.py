# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
db_config={
    host='127.0.0.1',
    user='root',
    psw='13298422297',
    charset='utf8',
    use_unicode = False
}
def connection():
    conn = pymysql.connect(db_config)
    return conn

class JianshuPipeline(object):
    def process_item(self, item, spider):
        db_connect=connection()
        cursor=db_connect.cursor()
        cursor.execute('USE jianshu')
        return item
