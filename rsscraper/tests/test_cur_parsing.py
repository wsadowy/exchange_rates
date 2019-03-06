import unittest

from rsscraper.spiders.currency_rate_spider import CurrencySpider
from rsscraper.tests.responses import fake_response


class CurrencySpiderTest(unittest.TestCase):

    def setUp(self):
        self.spider = CurrencySpider()

    def test_parse(self):
        import pdb
        pdb.set_trace()
        results = self.spider.parse(fake_response('responses/sample1.xml'))
        self._test_results(results)

    def _test_results(self, results):
        pass
