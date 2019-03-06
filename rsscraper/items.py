# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem

from rates_api.models import CurrencyRate


class CurrencyRateItem(DjangoItem):
    django_model = CurrencyRate
