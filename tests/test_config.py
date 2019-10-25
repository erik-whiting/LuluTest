import unittest

from configs.page_configs import PageConfig


class TestConfigs(unittest.TestCase):
    test_url = 'http://www.eriktest.com'
    cf = PageConfig(test_url)

    def test_returns_url(self):
        self.assertEqual(self.test_url, self.cf.url())

    def test_http_toggle(self):
        self.cf.https()
        self.assertEqual('https://', self.cf.http_prefix)
        self.cf.http()
        self.assertEqual('http://', self.cf.http_prefix)
        self.assertEqual(self.test_url, self.cf.url())