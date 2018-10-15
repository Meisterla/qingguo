# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter
import pymysql.cursors
import logging

class QingguoPipeline(object):
    def open_spider(self, spider):
        self.file = open('C:\\Users\\Administrator\\Desktop\\数据分析\\qingguo.csv', 'wb')#Running time
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

class QingguoPipelineMysql(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',  # 数据库地址
            port=3306,  # 数据库端口
            db='qingguo',  # 数据库名
            user='root',  # 数据库用户名
            passwd='123456',  # 数据库密码
            charset='utf8',  # 编码方式
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor();

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                """insert into qingguo.novel(novel.novel_name, novel.novel_author, novel.novel_tag, novel.novel_zishu ,novel.novel_redu, novel.novel_shoucang, novel.novel_status, novel.novel_introduction, novel.novel_startdate, novel.novel_updatedate, novel.novel_url)
                value (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (item['novel_name'].strip('\n').strip(),
                 item['novel_author'].strip('\n').strip(),
                 item['novel_tag'].strip('\n').strip(),
                 item['novel_zishu'].strip('\n').strip(),
                 item['novel_redu'].strip('\n').strip(),
                 item['novel_shoucang'].strip('\n').strip(),
                 item['novel_status'].strip('\n').strip(),
                 item['novel_introduction'].strip('\n').strip(),
                 item['novel_startdate'],
                 item['novel_updatedate'],
                 item['novel_url']))
            # 提交sql语句
            self.connect.commit()
        except Exception as error:
            logging.log(error)
        return item  # 必须实现返回
