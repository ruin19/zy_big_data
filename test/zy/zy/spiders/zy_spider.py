# -*- coding: utf-8 -*-
import scrapy


class ZySpiderSpider(scrapy.Spider):
    name = "zy_spider"
    allowed_domains = ["sz.centanet.com"]
    start_urls = (
        'http://sz.centanet.com/chengjiao/',
    )

    def parse(self, response):
        with open('zy_data', 'wb') as f:
            # f.write(response.body)
            for one_cj_data in response.xpath('//div[@class="cj_fy_box"]/ul/li'):
                garden_name = one_cj_data.xpath('.//div[@class="cjfy_xx esfbt"]/node()[last()]').extract()[0]
                print garden_name
                f.write(garden_name)

