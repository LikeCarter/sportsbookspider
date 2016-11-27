# -*- coding: utf-8 -*-
import scrapy
import datetime

from dtmto.items import DtmtoItem

class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["sportsbookreview.com"]
    end_date = '20120407'
    start_urls = (
        'http://www.sportsbookreview.com/nhl-hockey/odds-scores/20111006/',
    )

    def parse(self, response):
		full_url = response.url
		if len(response.css('.tbl-odds-time h1::text').extract()) != 1:
			for table in response.css('.tbl-odds'):
				item = DtmtoItem()
				item['date'] = datetime.datetime.strptime(full_url.split('/')[5], '%Y%m%d').strftime('%m-%d-%y')
				item['home'] = table.css('.tbl-odds-team0::text').extract()[0]
				item['visitor'] = table.css('.tbl-odds-team0::text').extract()[1]
				item['homescore'] = table.css('.tbl-odds-c3 nobr::text').extract()[0]
				item['visitorscore'] = table.css('.tbl-odds-c3 nobr::text').extract()[1]

				item['homeML'] = table.css('.tbl-odds-c5 nobr div::text').extract()[0].replace('+','')
				item['visitorML'] = table.css('.tbl-odds-c5 nobr div::text').extract()[1].replace('+','')
				
				totalhome = table.css('.tbl-odds-c7 nobr div::text').extract()[0].encode('utf-8')
				item['over'] = "N/A"
				item['ou'] = "N/A"
				if "N/A" not in totalhome:
					totalhome = table.css('.tbl-odds-c7 nobr div::text').extract()[0].encode('utf-8').replace('\xc2', '').replace('\xbd','.5').split('\xa0')
					item['ou'] = totalhome[0]
					over = totalhome[1]
					item['over'] = over.replace('+','')
				
				
				totalvisitor = table.css('.tbl-odds-c7 nobr div::text').extract()[1].encode('utf-8')
				item['under'] = "N/A"
				if "N/A" not in totalvisitor:
					totalvisitor = table.css('.tbl-odds-c7 nobr div::text').extract()[1].encode('utf-8').replace('\xc2', '').replace('\xbd','.5').split('\xa0')
					under = totalvisitor[1]
					item['under'] = under.replace('+','')
				

				yield item

		next_url = response.css('.mini-calendar a::attr(href)').extract()[1]
		if (next_url.split('/')[5] != self.end_date):
			print 'Next one!'
			yield scrapy.Request(next_url, callback=self.parse)