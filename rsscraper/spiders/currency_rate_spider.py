from decimal import Decimal
from os import path

import scrapy
from dateutil.parser import parse

from rsscraper.items import CurrencyRateItem


class CurrencySpider(scrapy.Spider):
    name = "currency_spider"
    main_url = "https://www.ecb.europa.eu"
    start_urls = [path.join(main_url, "home/html/rss.en.html")]
    ns = {
        "d": "http://purl.org/rss/1.0/",
        "cb": "http://www.cbwiki.net/wiki/index.php/Specification_1.1",
        "dc": "http://purl.org/dc/elements/1.1/",
    }

    @classmethod
    def _parse_currency_details(cls, response):
        item_nodes = response.xpath('d:item', namespaces=cls.ns)
        if not item_nodes:
            return
        for node in item_nodes:
            rate_node = node.xpath('cb:statistics/cb:exchangeRate', namespaces=cls.ns)
            date_str = node.xpath('dc:date/text()', namespaces=cls.ns).get()
            item = CurrencyRateItem()
            item['currency'] = rate_node.xpath('cb:targetCurrency/text()', namespaces=cls.ns).get()
            item['rate'] = Decimal(rate_node.xpath('cb:value/text()', namespaces=cls.ns).get())
            item['rate_from'] = parse(date_str).date()
            yield item

    def parse(self, response):
        data = response.xpath('//*[@id="ecb-content-col"]/main/ul[2]/li')
        for li in data:
            appendix = li.xpath('a/@href').get()
            if not appendix:
                continue
            currency_url = response.urljoin(appendix)
            request = scrapy.Request(currency_url, callback=self._parse_currency_details)
            yield request
