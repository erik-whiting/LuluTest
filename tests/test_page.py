import unittest

from page import *
from element import *
from action import Action


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

    def test_drag_drop(self):
        p = Page('https://the-internet.herokuapp.com/drag_and_drop')
        actions = Action()
        actions.go(p)

        p.elements = [
            PageElement(("xpath", "(//div[@id='columns']/div)[1]"), 'first'),
            PageElement(("xpath", "(//div[@id='columns']/div)[2]"), 'last'),
            PageElement(('id', 'column-a'), 'column-a'),
            PageElement(('id', 'column-b'), 'column-b')
        ]

        self.assertEqual(actions.get_attribute(p.get_element('first'), 'innerHTML'),
                         actions.get_attribute(p.get_element('column-a'), 'innerHTML'))
        self.assertEqual(actions.get_attribute(p.get_element('last'), 'innerHTML'),
                         actions.get_attribute(p.get_element('column-b'), 'innerHTML'))

        actions.drag_drop(p.get_element('column-a'), p.get_element('column-b'))

        # these should fail
        self.assertEqual(actions.get_attribute(p.get_element('first'), 'innerHTML'),
                         actions.get_attribute(p.get_element('column-a'), 'innerHTML'))
        self.assertEqual(actions.get_attribute(p.get_element('last'), 'innerHTML'),
                         actions.get_attribute(p.get_element('column-b'), 'innerHTML'))

        actions.close()
