import unittest

from LuluTest.page import Page
from LuluTest.element import PageElement, AlertElement
from LuluTest.action import Action
from LuluTest.step import *


class TestOtherPages(unittest.TestCase):

    def test_saucedemo_refresh_page(self):
        page = Page('https://www.saucedemo.com/inventory.html')
        actions = Action()
        actions.go(page)

        page.elements = [
            PageElement(('id', 'user-name'), 'username field'),
            PageElement(('id', 'password'), 'password field'),
            PageElement(('id', 'login-button'), 'login button'),
            PageElement(("id", "add-to-cart-sauce-labs-backpack"), "button 1"),
            PageElement(("xpath", '//*[@id="item_4_title_link"]/div'), "inventory item"),
            PageElement(("class", "shopping_cart_badge"), "shopping cart badge"),
            PageElement(("class", "inventory_item_name"), "item name")
        ]

        login = Steps(actions, [
            ('type', page.get_element('username field'), 'standard_user'),
            ('type', page.get_element('password field'), 'secret_sauce'),
            ('click', page.get_element('login button'))
        ])
        Do(login)

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
        import os  # Need this to work locally and in remote CI
        base_path = os.getcwd()
        if 'tests' in base_path:
            pass
        else:
            base_path += '/tests'

        page = Page('http://the-internet.herokuapp.com/upload')
        actions = Action()
        actions.go(page)
        page.elements = [
            PageElement(('id', 'file-upload'), 'Upload Element'),
            PageElement(('id', 'file-submit'), 'Submit Button')
        ]
        file_path = base_path + '/fixtures/files/upload_text_file.txt'
        actions.upload_file(page.get_element('Upload Element'), file_path)
        actions.click(page.get_element('Submit Button'))

        success_text = 'File Uploaded!'
        self.assertIn(success_text, actions.get_page_source())

    def test_dropdown(self):
        page = Page('http://the-internet.herokuapp.com/dropdown')
        actions = Action()
        actions.go(page)
        dropdown = PageElement(('id', 'dropdown'), 'dropdown')
        option_2 = PageElement(('xpath', '/html/body/div[2]/div/div/select/option[3]'), 'option 2')
        actions.select_drop_down(dropdown, 'Option 2')
        is_selected = actions.get_attribute(option_2, 'selected')
        self.assertTrue(is_selected)

    def test_script_execution(self):
        page = Page('https://demoqa.com/accordian/')
        actions = Action()
        actions.go(page)
        click_header_script = 'document.getElementById("section2Heading").click()'
        div_class_name = 'return document.getElementById("section2Content").parentElement.className'
        self.assertEqual(actions.execute_script(div_class_name), 'collapse')
        actions.execute_script(click_header_script)
        self.assertEqual(actions.execute_script(div_class_name), 'collapsing')
