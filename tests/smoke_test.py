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
