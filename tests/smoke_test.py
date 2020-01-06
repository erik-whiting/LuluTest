import unittest

from lulu_exceptions import PageNotLoadedError
from page import Page
from element import PageElement
from action import Action


class SmokeTest(unittest.TestCase):
    def test_smoke_test(self):
        erik_whiting = Page('http://erikwhiting.com')
        link = PageElement(('Link Text', 'blog'), 'blog link')
        actions = Action()
        actions.go(erik_whiting)
        actions.click(link)
        url = actions.get_url()
        self.assertEqual(url, 'https://blog.erikwhiting.com/')

    def test_page_not_loaded_exception(self):
        actions = Action()
        self.assertRaises(PageNotLoadedError, actions.get_url)

    def test_write_and_click(self):
        page = Page('http://erikwhiting.com/newsOutlet')
        actions = Action()
        page.elements = [
            PageElement(("id", "sourceNews"), "input box"),
            PageElement(("id", "transmitter"), "button"),
            PageElement(("id", "en1"), "english div")
        ]
        actions.go(page)
        actions.input_text(page.get_element("input box"), "Hello")
        actions.click(page.get_element("button"))
        english_div = page.get_element("english div")
        english_text = actions.check_element_text(english_div, "Hello")
        self.assertTrue(english_text)
        actions.close()