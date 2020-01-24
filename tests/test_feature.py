import unittest

from page import Page
from element import PageElement
from action import Action


class TestFeature(unittest.TestCase):
    page = Page('http://erikwhiting.com/newsOutlet')
    page.elements = [
        PageElement(("id", "sourceNews"), "input box"),
        PageElement(("id", "transmitter"), "button"),
        PageElement(("id", "en1"), "english div")
    ]

    def setUp(self):
        self.actions = Action()
        self.actions.go(self.page)

    def tearDown(self):
        self.actions.close()
        del self.actions

    def test_page_source_feature(self):
        source = self.actions.get_page_source()
        self.assertIn('<body onload="defaultBreaking()">', source)

    def test_page_refresh(self):
        self.actions.refresh()
        current_url = self.actions.get_url()
        self.assertEqual('http://erikwhiting.com/newsOutlet/', current_url)

    def test_page_change_url(self):
        current_url = self.actions.get_url()
        self.assertEqual('http://erikwhiting.com/newsOutlet/', current_url)

        self.actions.go_to('https://github.com')
        current_url = self.actions.get_url()
        self.assertEqual('https://github.com/', current_url)
