import unittest

from LuluTest.page import Page
from LuluTest.element import PageElement
from LuluTest.action import Action


class TestBrowsers(unittest.TestCase):
    page = Page('http://erikwhiting.com/newsOutlet')
    page.elements = [
        PageElement(("id", "sourceNews"), "input box"),
        PageElement(("id", "transmitter"), "button"),
        PageElement(("id", "en1"), "english div")
    ]
    actions = None

    def _set_up(self, browser):
        self.actions = Action(browser)
        self.actions.go(self.page)

    def tearDown(self):
        self.actions.close()
        del self.actions

    def test_page_source_feature_chrome(self):
        self._set_up('Chrome')
        source = self.actions.get_page_source()
        self.assertIn('<body onload="defaultBreaking()">', source)

    def test_page_refresh_chrome(self):
        self._set_up('Chrome')
        self.actions.refresh()
        current_url = self.actions.get_url()
        self.assertEqual('http://erikwhiting.com/newsOutlet/', current_url)

    def test_page_change_url_chrome(self):
        self._set_up('Chrome')
        current_url = self.actions.get_url()
        self.assertEqual('http://erikwhiting.com/newsOutlet/', current_url)

        self.actions.go_to('https://github.com')
        current_url = self.actions.get_url()
        self.assertEqual('https://github.com/', current_url)

    def test_page_source_feature_firefox(self):
        self._set_up('Firefox')
        source = self.actions.get_page_source()
        self.assertIn('<body onload="defaultBreaking()">', source)

    def test_page_refresh_firefox(self):
        self._set_up('Firefox')
        self.actions.refresh()
        current_url = self.actions.get_url()
        self.assertEqual('http://erikwhiting.com/newsOutlet/', current_url)

    def test_page_change_url_firefox(self):
        self._set_up('Firefox')
        current_url = self.actions.get_url()
        self.assertEqual('http://erikwhiting.com/newsOutlet/', current_url)

        self.actions.go_to('https://github.com')
        current_url = self.actions.get_url()
        self.assertEqual('https://github.com/', current_url)