# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
db_config={
    'host':'127.0.0.1',
    'user':'root',
    'psw':'13298422297',
    'charset':'utf8',
    'use_unicode' : False
}
def connection():
    conn = pymysql.connect(db_config)
    return conn

class JianshuPipeline(object):
    def process_item(self, item, spider):
        db_connect=connection()
        cursor=db_connect.cursor()
        cursor.execute('USE jianshu')
        sql = 'INSERT INTO articals(author,title,pulish_time,abstract,read_number,comment_number,collect_number,item_url)VALUS(%s,%s,%s,%s,%s,%s,%s,%s)'
        try:
            cursor.execute(sql,(item['author'],item['title'],item['pulish_time'],item['abstract'],item['read_number'],item['comment_number'],item['collect_number'],item['item_url']))
        except expression as e:
            print('错误信息》》》》',e,'《《《《错误信息')
        return item
