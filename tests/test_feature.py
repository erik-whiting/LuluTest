import unittest

from configs.page_configs import PageConfig
from page.page import Page
from step.step import Step
from tests import helpers as helper


class TestFeature(unittest.TestCase):
    cf = PageConfig('erikwhiting.com/newsOutlet')
    cf.options_list.append("headless")
    bp = None

    @classmethod
    def setUp(cls):
        cls.bp = Page(cls.cf)
        cls.bp.go()

    @classmethod
    def tearDown(cls):
        cls.bp.close()

    def test_write_and_click_with_headless(self):
        self.bp.collect_elements([
            ("id", "sourceNews", "input box"),
            ("id", "transmitter", "button"),
            ("id", "en1", "english div")
        ])
        self.bp.element("input box").input_text("Hello")
        self.bp.element("button").click()
        english_div = helper.evaluate_element_text(self.bp.element("english div"), "Hello")
        self.assertTrue(english_div)

    def test_page_source_feature(self):
        source = self.bp.page_source()
        self.assertIn('<body onload="defaultBreaking()">', source)

    def test_page_url(self):
        current_url = self.bp.get_url()
        if current_url[current_url.__len__() - 1] == "/":
            current_url = current_url[:-1]
        self.assertEqual(self.cf.url(), current_url)

    def test_page_refresh(self):
        self.bp.refresh()
        current_url = self.bp.get_url()
        if current_url[current_url.__len__() - 1] == "/":
            current_url = current_url[:-1]
        self.assertEqual(self.cf.url(), current_url)

    def test_page_change_url(self):
        current_url = self.bp.get_url()
        if current_url[current_url.__len__() - 1] == "/":
            current_url = current_url[:-1]
        self.assertEqual(self.cf.url(), current_url)

        self.bp.navigate_to('https://github.com')
        current_url = self.bp.get_url()
        if current_url[current_url.__len__() - 1] == "/":
            current_url = current_url[:-1]
        self.assertEqual('https://github.com', current_url)

    def test_do(self):
        self.bp.collect_elements([
            ("id", "sourceNews"),
            ("id", "transmitter")
        ])
        input_element = self.bp.elements[0]
        transmit_button = self.bp.elements[1]
        steps = [
            Step("type", input_element, "Hello"),
            Step("click", transmit_button)
        ]
        self.bp.do(steps)
        english_div = helper.evaluate_element_text(
            self.bp.grab("id", "en1"),
            "Hello"
        )
        self.assertTrue(english_div)

    def test_named_elements(self):
        self.bp.collect_elements([
            ("id", "sourceNews", "input"),
            ("id", "transmitter", "button")
        ])
        steps = [
            Step("type", self.bp.element("input"), "Hello"),
            Step("click", self.bp.element("button"))
        ]
        self.bp.do(steps)
        english_div = helper.evaluate_element_text(self.bp.grab("id", "en1"), "Hello")
        self.assertTrue(english_div)
