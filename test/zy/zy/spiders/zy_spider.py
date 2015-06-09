# -*- coding: utf-8 -*-
import scrapy
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class HouseTrade():
    garden_name =''
    garden_price = ''
    trade_date = ''
    garden_sumPrice = ''

    def getInfo(self):
        return self.garden_name + "," + self.garden_price +"," + self.trade_date + "," + self.garden_sumPrice + ","


class ZySpiderSpider(scrapy.Spider):
    name = "zy_spider"
    allowed_domains = ["sz.centanet.com"]
    start_urls = (
        'http://sz.centanet.com/chengjiao/',
    )

    def getnextpage(self, response):
        for buttom_data in response.xpath('//div[@class="bottom-paging"]/div[@class="zjfy"]'):
            nextpage = buttom_data.xpath('//div[@class="fy2"]/a/@href').extract()[-1]
            return nextpage
        
    def getnextpage_text(self, response):
        for buttom_data in response.xpath('//div[@class="bottom-paging"]/div[@class="zjfy"]'):
            nextpage = buttom_data.xpath('//div[@class="fy2"]/a/text()').extract()[-1]
            return nextpage

    def parse(self, response):
        with open('zy_data.csv', 'a+') as f:
            # f.write(response.body)
            #for buttom_data in response.xpath('//div[@class="bottom-paging"]/div[@class="zjfy"]'):
            #    nextpage = buttom_data.xpath('//div[@class="fy2"]/a/@href').extract()[0]
            #    print nextpage
                
            for one_cj_data in response.xpath('//div[@class="cj_fy_box"]/ul/li'):
                houseTrade = HouseTrade();
                houseTrade.garden_name = one_cj_data.xpath('.//div[@class="cjfy_xx esfbt"]/node()[last()]').extract()[0]
                houseTrade.garden_price = one_cj_data.xpath('.//div[@class="time_zy"]/span[@class="red22"]/node()').extract()[0]
                houseTrade.trade_date = one_cj_data.xpath('.//div[@class="time_zy"]/span[@class="black24"]/node()').extract()[0]
                houseTrade.garden_sumPrice = one_cj_data.xpath('.//div[@class="zj_zy"]/span[@class="red22"]/node()').extract()[0]

                houseTrade.garden_price = houseTrade.garden_price.strip("元/平")
                houseTrade.garden_sumPrice = houseTrade.garden_sumPrice.strip("万")
                
                
                print houseTrade.garden_name
                print houseTrade.garden_price
                print houseTrade.trade_date
                print houseTrade.garden_sumPrice              
                f.write(houseTrade.getInfo())
            f.close()

            nextpageText = self.getnextpage_text(response)
            print nextpageText

            if nextpageText == "末页":
                print "Search next pages"
                nextpage = self.getnextpage(response)
                next_urls = 'http://sz.centanet.com' + nextpage
                yield scrapy.Request(next_urls, callback=self.parse)
            
            
                

    

