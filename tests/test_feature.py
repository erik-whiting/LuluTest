import unittest

from configs.config import Config
from page.page import Page
from page.step import Step
from .helpers import evaluate_element_text


class TestFeature(unittest.TestCase):
    cf = Config()
    cf.base_url = 'erikwhiting.com'
    cf.subdomain = ''
    cf.base_url += '/newsOutlet'

    def test_write_and_click_with_headless(self):
        self.cf.options_list = ["headless"]
        bp = Page(self.cf)
        bp.go()
        bp.element_by("id", "sourceNews").input_text("Hello")
        bp.element_by("id", "transmitter").click()
        english_div = evaluate_element_text(bp.element_by("id", "en1"), "Hello")
        self.assertTrue(english_div)
        bp.close()

    def test_page_source_feature(self):
        self.cf.options_list = ["headless"]
        bp = Page(self.cf)
        bp.go()
        source = bp.page_source()
        self.assertIn('<body onload="defaultBreaking()">', source)
        bp.close()

    def test_page_url(self):
        self.cf.options_list = ["headless"]
        bp = Page(self.cf)
        bp.go()
        current_url = bp.get_url()
        if current_url[current_url.__len__() - 1] == "/":
            current_url = current_url[:-1]
        self.assertEqual(self.cf.url(), current_url)
        bp.close()

    def test_page_refresh(self):
        self.cf.options_list = ["headless"]
        bp = Page(self.cf)
        bp.go()

        bp.refresh()
        current_url = bp.get_url()
        if current_url[current_url.__len__() - 1] == "/":
            current_url = current_url[:-1]
        self.assertEqual(self.cf.url(), current_url)
        bp.close()

    def test_page_change_url(self):
        self.cf.options_list = ["headless"]
        bp = Page(self.cf)
        bp.go()

        current_url = bp.get_url()
        if current_url[current_url.__len__() - 1] == "/":
            current_url = current_url[:-1]
        self.assertEqual(self.cf.url(), current_url)

        bp.navigate_to('https://github.com')
        current_url = bp.get_url()
        if current_url[current_url.__len__() - 1] == "/":
            current_url = current_url[:-1]
        self.assertEqual('https://github.com', current_url)
        bp.close()

    def test_do_step(self):
        self.cf.options_list.append("headless")
        bp = Page(self.cf)
        bp.go()
        input_element = bp.element_by("id", "sourceNews")
        transmit_button = bp.element_by("id", "transmitter")
        bp.do_step("type", input_element, "Hello")
        bp.do_step("click", transmit_button)
        english_div = evaluate_element_text(bp.element_by("id", "en1"), "Hello")
        self.assertTrue(english_div)
        bp.close()

    def test_do(self):
        self.cf.options_list.append("headless")
        bp = Page(self.cf)
        bp.go()
        input_element = bp.element_by("id", "sourceNews")
        transmit_button = bp.element_by("id", "transmitter")
        steps = [
            Step("type", input_element, "Hello"),
            Step("click", transmit_button)
        ]
        bp.do(steps)
        english_div = evaluate_element_text(bp.element_by("id", "en1"), "Hello")
        self.assertTrue(english_div)
        bp.close()

    def test_element_collection_and_steps(self):
        self.cf.options_list.append("headless")
        bp = Page(self.cf)
        bp.go()
        bp.collect_elements([
            ("id", "sourceNews"),
            ("id", "transmitter")
        ])
        steps = [
            Step("type", bp.elements[0], "Hello"),
            Step("click", bp.elements[1])
        ]
        bp.do(steps)
        english_div = evaluate_element_text(bp.element_by("id", "en1"), "Hello")
        self.assertTrue(english_div)
        bp.close()

    def test_named_elements(self):
        self.cf.options_list.append("headless")
        bp = Page(self.cf)
        bp.go()
        bp.collect_elements([
            ("id", "sourceNews", "input"),
            ("id", "transmitter", "button")
        ])
        steps = [
            Step("type", bp.element("input"), "Hello"),
            Step("click", bp.element("button"))
        ]
        bp.do(steps)
        english_div = evaluate_element_text(bp.element_by("id", "en1"), "Hello")
        self.assertTrue(english_div)
        bp.close()
