import unittest

from element import *


class TestElements(unittest.TestCase):
    def test_page_element(self):
        el = PageElement(Locator('id', 'test'), 'test element')
        self.assertTupleEqual(el.locator, ('id', 'test'))
        self.assertEqual(el.name, 'test element')
        self.assertFalse(el.is_alert_element)
        self.assertTrue(el.is_page_element)

    def test_alert_element(self):
        el = AlertElement('test element')
        self.assertEqual(el.name, 'test element')
        self.assertFalse(el.is_page_element)
        self.assertTrue(el.is_alert_element)
