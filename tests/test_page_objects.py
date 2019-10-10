import unittest

from configs.config import Config
from page.page import Page
from page.page_element import PageElement


class TestBasePage(unittest.TestCase):
    cf = Config()
    cf.driver = 'TestDriver'
    cf.base_url = 'TestMe.com'

    def test_base_page_returns_config_url(self):
        bp = Page(self.cf)
        self.assertEqual(bp.url, self.cf.url())

    def test_base_page_returns_config_url_with_sub_dir(self):
        bp = Page(self.cf, 'about')
        self.assertEqual(bp.url, self.cf.url() + '/about')

    def test_page_knows_its_headless(self):
        self.cf.options_list = ['headless']
        bp = Page(self.cf)
        self.assertIn("headless", bp.options_list)

    def test_page_knows_its_not_headless(self):
        self.cf.options_list = []
        bp = Page(self.cf)
        self.assertNotIn("headless", bp.options_list)

    def test_anonymous_elements(self):
        cf = Config()
        cf.base_url = 'erikwhiting.com'
        cf.subdomain = ''
        cf.base_url += '/newsOutlet'
        cf.options_list = ['headless']
        bp = Page(cf)
        bp.go()
        elem = ("id", "transmitter")
        bp.collect_elements([elem])
        element = bp.element(0)
        self.assertTrue(isinstance(element, PageElement))
        bp.close()

    def test_named_elements(self):
        cf = Config()
        cf.base_url = 'erikwhiting.com'
        cf.subdomain = ''
        cf.base_url += '/newsOutlet'
        cf.options_list = ['headless']
        bp = Page(cf)
        bp.go()
        elem = ("id", "transmitter", "name")
        bp.collect_elements([elem])
        element = bp.element("name")
        self.assertTrue(isinstance(element, PageElement))
        bp.close()
