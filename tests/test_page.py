import unittest

from LuluTest import PageElement, Locator
from LuluTest.page import Page


class TestPage(unittest.TestCase):
    page = Page('www.example.com')
    element = PageElement(Locator('id', 'test'), 'test')

    def test_basic_page(self):
        self.assertEqual(self.page.url, 'www.example.com')

    def test_init_with_elements(self):
        p = Page('www.example.com', [self.element])
        self.assertEqual(p.url, 'www.example.com')
        self.assertEqual(len(p.elements), 1)

    def test_add_element(self):
        self.assertEqual(len(self.page.elements), 0)
        self.page.elements.append(self.element)
        self.assertEqual(len(self.page.elements), 1)

    def test_get_element_from_page(self):
        p = Page('www.example.com', [self.element])
        element_by_index = p.elements[0]
        self.assertEqual(element_by_index, self.element)
        element_by_name = [elem for elem in p.elements if elem.name == 'test'][0]
        self.assertEqual(element_by_name, self.element)
