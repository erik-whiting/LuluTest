import unittest

from page import Page
from element import PageElement, AlertElement
from action import Action
from step import *


class TestOtherPages(unittest.TestCase):
    def test_saucedemo_page(self):
        page = Page('https://www.saucedemo.com/inventory.html')
        actions = Action()
        actions.go(page)

        page.elements = [
            PageElement(("xpath", "(//button[@class='btn_primary btn_inventory'])[1]"), "inv_btn1"),
            PageElement(("xpath", "(//button[@class='btn_primary btn_inventory'])[2]"), "inv_btn2"),
            PageElement(("xpath", "(//button[@class='btn_primary btn_inventory'])[3]"), "inv_btn3"),
            PageElement(("class", "shopping_cart_badge"), "Cart Badge"),
            PageElement(("class", "shopping_cart_link"), "Cart Link"),
            PageElement(("class", "cart_button"), "Cart Button"),
            PageElement(("class", "checkout_button"), "Checkout Button"),
            PageElement(("id", "first-name"), "First Name"),
            PageElement(("id", "last-name"), "Last Name"),
            PageElement(("id", "postal-code"), "Zip"),
            PageElement(("class", "complete-header"), "Completion Header")
        ]

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

    def test_saucedemo_refresh_page(self):
        page = Page('https://www.saucedemo.com/inventory.html')
        actions = Action()
        actions.go(page)

        page.elements = [
            PageElement(("xpath", "(//button[@class='btn_primary btn_inventory'])[1]"), "button 1"),
            PageElement(("xpath", "(//div[@class='inventory_item_name'])[1]"), "inventory item"),
            PageElement(("class", "shopping_cart_badge"), "shopping cart badge"),
            PageElement(("class", "inventory_item_name"), "item name")
        ]

        actions.click(page.get_element("button 1"))
        item_name = actions.get_attribute(page.get_element("inventory item"), "innerHTML")
        items_in_cart = actions.get_attribute(page.get_element("shopping cart badge"), "innerHTML")

        self.assertEqual(items_in_cart, "1")
        actions.refresh()
        items_in_cart = actions.get_attribute(page.get_element("shopping cart badge"), "innerHTML")
        self.assertEqual(items_in_cart, "1")

        actions.go_to('https://www.saucedemo.com/cart.html')
        inventory_item_name = actions.get_attribute(page.get_element("item name"), "innerHTML")
        self.assertEqual(item_name, inventory_item_name)
        actions.close()

    def test_javascript_alert(self):
        page = Page('https://the-internet.herokuapp.com/javascript_alerts')
        actions = Action()
        actions.go(page)

        to_be_clicked = PageElement(('xpath', "(//button)[1]"))
        actions.click(to_be_clicked)
        alert = AlertElement()
        js_text = actions.get_text(alert)
        self.assertEqual(js_text, "I am a JS Alert")
        actions.accept(alert)
        actions.close()

    def test_javascript_confirm(self):
        page = Page('https://the-internet.herokuapp.com/javascript_alerts')
        actions = Action()
        actions.go(page)

        to_be_clicked = PageElement(('xpath', "(//button)[2]"))
        actions.click(to_be_clicked)
        alert = AlertElement()
        js_text = actions.get_text(alert)
        self.assertEqual(js_text, "I am a JS Confirm")
        actions.dismiss(alert)
        actions.close()

    def test_javascript_prompt(self):
        page = Page('https://the-internet.herokuapp.com/javascript_alerts')
        actions = Action()
        actions.go(page)
        page.elements = [
            PageElement(("xpath", "(//button)[3]"), "prompt button"),
            PageElement(("id", "result"), "result"),
            AlertElement('alert')
        ]

        actions.click(page.get_element("prompt button"))
        alert_text = actions.get_text(page.get_element('alert'))
        self.assertEqual(alert_text, "I am a JS prompt")
        actions.input_text(page.get_element('alert'), 'This is a test')
        actions.accept(page.get_element('alert'))

        result = actions.get_attribute(page.get_element('result'), 'innerHTML')
        self.assertEqual(result, "You entered: This is a test")
        actions.close()

    def test_file_upload(self):
        page = Page('http://the-internet.herokuapp.com/upload')
        actions = Action()
        actions.go(page)
        page.elements = [
            PageElement(('id', 'file-upload'), 'Upload Element'),
            PageElement(('id', 'file-submit'), 'Submit Button')
        ]

        file_path = 'C:\\Users\\eedee\\LuluTest\\.tmp\\upload_text_file.txt'
        actions.upload_file(page.get_element('Upload Element'), file_path)
        actions.click(page.get_element('Submit Button'))

        success_text = 'File Uploaded!'
        self.assertIn(success_text, actions.get_page_source())
