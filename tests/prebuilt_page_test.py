import unittest
from LuluTest.action import *
from LuluTest.step import *
from LuluTest.page import page_factory


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
        url = actions.get_url()
        self.assertEqual(url, page.url + '/')
        actions.close()

    def test_complicated_page(self):
        page = self.pages['inventory']
        actions = Action()
        actions.go(page)

        login = Steps(actions, [
            ('type', page.get_element('user_name'), 'standard_user'),
            ('type', page.get_element('password'), 'secret_sauce'),
            ('click', page.get_element('login_button'))
        ])

        Do(login)

        steps = Steps(actions, [
            ('click', page.get_element('inv_btn1')),
            ('click', page.get_element('inv_btn2')),
            ('click', page.get_element('inv_btn3'))
        ])

        Do(steps)
        items_in_cart = actions.get_attribute(page.get_element("Cart Badge"), "innerHTML")
        # Test is flaky here, sometimes it checks the cart value
        # before the cart is updated.
        self.assertEqual(items_in_cart, "3")

        actions.click(page.get_element("Cart Link"))
        actions.click(page.get_element("Remove Button"))
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
