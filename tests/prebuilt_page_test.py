import unittest

from action import Action
from step import Do, Steps
from page import page_factory


class PrebuiltPageTest(unittest.TestCase):
    import os  # Need this to work locally and in remote CI
    base_path = os.getcwd()
    if 'tests' in base_path:
        pass
    else:
        base_path += '/tests'

    prebuilt_pages_directory = base_path + '/fixtures/pages/'
    page_configs = [
        prebuilt_pages_directory + 'news_outlet.json',
        prebuilt_pages_directory + 'inventory.yml'
    ]
    pages = page_factory.generate_pages(page_configs)

    def test_basic_usage(self):
        page = self.pages['news_outlet']
        actions = Action()
        actions.go(page)
        actions.input_text(page.get_element("input_box"), "Hello")
        actions.click(page.get_element("button"))
        english_div = page.get_element("english_div")
        english_text = actions.check_element_text(english_div, "Hello")
        self.assertTrue(english_text)
        actions.close()

    def test_complicated_page(self):
        page = self.pages['inventory']
        actions = Action()
        actions.go(page)

        steps = Steps(actions, [
            ('click', page.get_element('inv_btn1')),
            ('click', page.get_element('inv_btn2')),
            ('click', page.get_element('inv_btn3'))
        ])

        Do(steps)
        items_in_cart = actions.get_attribute(page.get_element("Cart Badge"), "innerHTML")
        self.assertEqual(items_in_cart, "3")

        actions.click(page.get_element("Cart Link"))
        actions.click(page.get_element("Cart Button"))
        items_in_cart = actions.get_attribute(page.get_element("Cart Badge"), "innerHTML")
        self.assertEqual(items_in_cart, "2")
        actions.click(page.get_element("Checkout Button"))

        steps = Steps(actions, [
            ('type', page.get_element('First Name'), 'Jane'),
            ('type', page.get_element('Last Name'), 'Doe'),
            ('type', page.get_element('Zip'), '12345'),
            ('click', page.get_element('Cart Button'))
        ])
        Do(steps)

        actions.click(page.get_element("Cart Button"))
        checkout_complete_page = actions.get_attribute(page.get_element("Completion Header"), "innerHTML")
        self.assertEqual(checkout_complete_page, "THANK YOU FOR YOUR ORDER")

        actions.close()
