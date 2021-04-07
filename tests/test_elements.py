import unittest

from LuluTest.element.page_element import PageElement
from LuluTest.element.alert_element import AlertElement
from LuluTest.element.locator import Locator


class TestElements(unittest.TestCase):
    def test_page_element(self):
        el = PageElement(('id', 'test'), 'test element')
        self.assertTupleEqual(el.locator, ('id', 'test'))
        self.assertEqual(el.name, 'test element')
        self.assertFalse(el.is_alert_element)
        self.assertTrue(el.is_page_element)

    def test_alert_element(self):
        el = AlertElement('test element')
        self.assertEqual(el.name, 'test element')
        self.assertFalse(el.is_page_element)
        self.assertTrue(el.is_alert_element)

    def test_locator(self):
        test_locator = Locator('id', 'test')
        self.assertEqual(test_locator.by, 'id')
        self.assertEqual(test_locator.value, 'test')
