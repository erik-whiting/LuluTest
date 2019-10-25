import unittest

from configs.page_configs import PageConfig
from page.page import Page
from element.page_element import PageElement


class TestBasePage(unittest.TestCase):
    cf = PageConfig('TestMe.com')

    def test_page_knows_its_headless(self):
        self.cf.options_list = ['headless']
        bp = Page(self.cf)
        self.assertIn("headless", bp.options_list)

    def test_anonymous_elements(self):
        cf = PageConfig('erikwhiting.com/newsOutlet')
        cf.options_list = ['headless']
        bp = Page(cf)
        bp.go()
        elem = ("id", "transmitter")
        bp.collect_elements([elem])
        element = bp.element(0)
        self.assertTrue(isinstance(element, PageElement))
        bp.close()

    def test_named_elements(self):
        cf = PageConfig('erikwhiting.com/newsOutlet')
        cf.options_list = ['headless']
        bp = Page(cf)
        bp.go()
        elem = ("id", "transmitter", "name")
        bp.collect_elements([elem])
        element = bp.element("name")
        self.assertTrue(isinstance(element, PageElement))
        self.assertEqual(element.text, "Transmit!")
        bp.close()
