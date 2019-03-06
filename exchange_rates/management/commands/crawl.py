from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from rsscraper import settings as my_settings
from rsscraper.spiders.currency_rate_spider import CurrencySpider


class Command(BaseCommand):

    def handle(self, *args, **options):
        crawler_settings = Settings()
        crawler_settings.setmodule(my_settings)
        process = CrawlerProcess(settings=crawler_settings)
        process.crawl(CurrencySpider)
        process.start()
