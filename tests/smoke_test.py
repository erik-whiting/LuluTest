import unittest

from page import *
from element import *
from action import *
from page_element_interface import *


class SmokeTest(unittest.TestCase):
    def test_smoke_test(self):
        erik_whiting = Page('http://erikwhiting.com')
        link = PageElement(('Link Text', 'blog'), 'blog link')
        actions = Action(erik_whiting)
        actions.go()
        actions.click(link)
        url = actions.get_url()
        self.assertEqual(url, 'https://blog.erikwhiting.com/')