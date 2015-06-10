# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import json
from zy.items import ZyItem


class ZyPipeline(object):
    def __init__(self, *args, **kwargs):
        self.csvfile = csv.writer(open('big_data_csv.csv', 'wb'))
        self.file = open('items.jl', 'wb')
        return super(ZyPipeline, self).__init__(*args, **kwargs)

    def process_item(self, item, spider):
        print "begin process item"
        if item['garden_price']:
            item['garden_price'] = item['garden_price'].strip('元/平')
        if item['garden_sumPrice']:
            item['garden_sumPrice'] = item['garden_sumPrice'].strip('万')

        print item['garden_name']
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        self.csvfile.writerow([item['garden_name'], item['trade_date'], item['garden_price'], item['garden_sumPrice'], item['garden_detial'], item['garden_area'], item['garden_location'],])
        #self.csvfile.writerow(item)        
        return item
