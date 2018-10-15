# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
import re
from qingguo.items import QingguoItem

base_url = 'http://www.linovel.net'

class NovelSpider(scrapy.Spider):
    name = 'novel'
    allowed_domains = ['linovel.net']
    #start_urls = ['http://www.linovel.net/cat/-1.html/']
    page_url = 'http://www.linovel.net/cat/-1.html?page='
    offset = 1
    start_urls = [page_url + str(offset)]

    def parse(self, response):

        novel_url_list = response.xpath('//div[@class="wrapper"]//div[@class="content container book-info"]//div[@class="l-side col-sm-12 col-md-12"]//div[@class="works-grid row"]//a/@href')

        for novel in novel_url_list:
            novel_url = base_url + novel.extract()
            request = scrapy.Request(novel_url, callback=self.parse_novel)
            yield request
        if self.offset < 197:
            self.offset += 1
            url = self.page_url + str(self.offset)
            yield scrapy.Request(url, callback=self.parse)

        # novel_url_list_all = []
        # if self.offset < 197:
        #     for novel in novel_url_list:
        #         novel_url = base_url + novel.extract()
        #         novel_url_list_all.append(novel_url)
        #         self.offset = self.offset + 1
        #         url = self.page_url + str(self.offset)
        #         yield scrapy.Request(str(url), callback=self.parse)
        #
        # for i in range(len(novel_url_list)):
        #     novel_url_2 = novel_url_list[i]
        #     yield scrapy.Request(novel_url_2, callback=self.parse_novel)



    def parse_novel(self, response):
        novel_info = response.xpath('//div[@class="book-wrapper"]//div[@class="detail-layout"]//div[@class="detail hash-tab"]')
        novel_name = ''
        novel_name_list = novel_info.xpath('//div[@class="meta-info"]//h1[@class="book-title"]/text()').extract()
        for i in novel_name_list:
            novel_name += i

        novel_author = ''
        novel_author_list = response.xpath('//div[@class="book-wrapper"]//div[@class="detail-layout"]//div[@class="author-frame"]//div[@class="novelist"]//div[@class="name"]/a/text()').extract()
        for i in novel_author_list:
            novel_author += i

        novel_tag_list = novel_info.xpath('//div[@class="meta-info"]//div[@class="book-cats clearfix"]//a/text()')
        novel_tag = "|".join(str(i.extract()) for i in novel_tag_list)

        novel_zishu = ''
        novel_zishu_list = novel_info.xpath('//div[@class="meta-info"]//div[@class="book-data"]//span[1]/text()').extract()
        for i in novel_zishu_list:
            novel_zishu += i

        novel_redu = ''
        novel_redu_list = novel_info.xpath('//div[@class="meta-info"]//div[@class="book-data"]//span[3]/text()').extract()
        for i in novel_redu_list:
            novel_redu += i

        novel_shoucang = ''
        novel_shoucang_list = novel_info.xpath('//div[@class="meta-info"]//div[@class="book-data"]//span[5]/text()').extract()
        for i in novel_shoucang_list:
            novel_shoucang += i

        novel_status_list = novel_info.xpath('//div[@class="meta-info"]//div[@class="book-data"]//span[7]/text()').extract()
        novel_status = ''
        for i in novel_status_list:
            novel_status += i

        novel_introduction_list = novel_info.xpath('//div[@class="section introduction"]//div[@class="about-text text-content-actual"]/text()').extract()
        novel_introduction = ''
        for i in novel_introduction_list:
            novel_introduction += i

        novel_startdate = ''
        novel_startdate_list = response.xpath('//div[@class="book-wrapper"]//div[@class="detail-layout"]//div[@class="more-info-frame"]//div[@class="sub-list"]//div[@class="list filled"][1]//span/text()').extract()
        for i in novel_startdate_list:
            novel_startdate += i

        novel_updatedate = ''
        novel_updatedate_list = response.xpath('//div[@class="book-wrapper"]//div[@class="detail-layout"]//div[@class="more-info-frame"]//div[@class="sub-list"]//div[@class="list filled"][2]//span/text()').extract()
        for i in novel_updatedate_list:
            novel_updatedate += i

        novel_url = response.url

        item = QingguoItem()
        item['novel_name'] = novel_name
        item['novel_author'] = novel_author
        item['novel_tag'] = novel_tag
        item['novel_zishu']= novel_zishu
        item['novel_redu'] = novel_redu
        item['novel_shoucang'] = novel_shoucang
        item['novel_status'] = novel_status
        item['novel_introduction'] = novel_introduction
        item['novel_startdate'] = novel_startdate
        item['novel_updatedate'] = novel_updatedate
        item['novel_url'] = novel_url

        yield item

