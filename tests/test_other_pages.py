import unittest
from configs import config
from page import page, step


class TestOtherPages(unittest.TestCase):
	def test_calculator_page(self):
		cf = config.Config()
		cf.http_prefix = 'http://'
		cf.base_url = 'www.math.com/'
		cf.base_url += 'students/calculators/source/basic.htm'
		cf.options_list.append("headless")
		bp = page.Page(cf)
		bp.go()
		bp.element_by("name", "five").click()
		bp.element_by("name", "plus").click()
		bp.element_by("name", "seven").click()
		bp.element_by("name", "DoIt").click()
		answer = bp.element_by("name", "Input").get("value")
		self.assertEqual(answer, "12")
		bp.close()

	def test_saucedemo_page(self):
		cf = config.Config()
		cf.http_prefix = 'https://'
		cf.base_url = 'www.saucedemo.com/'
		cf.base_url += 'inventory.html'
		cf.options_list.append("headless")
		bp = page.Page(cf)
		bp.go()

		bp.collect_elements([
			("xpath", "(//button[@class='btn_primary btn_inventory'])[1]", "inv_btn1"),
			("xpath", "(//button[@class='btn_primary btn_inventory'])[2]", "inv_btn2"),
			("xpath", "(//button[@class='btn_primary btn_inventory'])[3]", "inv_btn3"),
		])
		steps = [
			step.Step("click", bp.element("inv_btn1")),
			step.Step("click", bp.element("inv_btn2")),
			step.Step("click", bp.element("inv_btn3"))
		]
		bp.do(steps)

		items_in_cart = bp.element_by("class", "shopping_cart_badge").get("innerHTML")
		self.assertEqual(items_in_cart, "3")

		bp.element_by("class", "shopping_cart_link").click()
		bp.element_by("class", "cart_button").click()
		items_in_cart = bp.element_by("class", "shopping_cart_badge").get("innerHTML")
		self.assertEqual(items_in_cart, "2")

		bp.element_by("class", "checkout_button").click()

		bp.collect_elements([
			("id", "first-name", "First Name"),
			("id", "last-name", "Last Name"),
			("id", "postal-code", "Zip"),
			("class", "cart_button", "Cart Button")
		])
		steps = [
			step.Step("type", bp.element("First Name"), "Jane"),
			step.Step("type", bp.element("Last Name"), "Doe"),
			step.Step("type", bp.element("Zip"), "12345"),
			step.Step("click", bp.element("Cart Button"))
		]
		bp.do(steps)

		bp.element_by("class", "cart_button").click()
		checkout_complete_page = bp.element_by("class", "complete-header").get("innerHTML")
		self.assertEqual(checkout_complete_page, "THANK YOU FOR YOUR ORDER")

		bp.close()

	def test_saucedemo_refresh_page(self):
		cf = config.Config()
		cf.http_prefix = 'https://'
		cf.base_url = 'www.saucedemo.com/'
		cf.base_url += 'inventory.html'
		cf.options_list.append("headless")
		bp = page.Page(cf)
		bp.go()

		bp.element_by("xpath", "(//button[@class='btn_primary btn_inventory'])[1]").click()
		item_name = bp.element_by("xpath", "(//div[@class='inventory_item_name'])[1]").get("innerHTML")
		items_in_cart = bp.element_by("class", "shopping_cart_badge").get("innerHTML")
		self.assertEqual(items_in_cart, "1")

		bp.go()

		items_in_cart = bp.element_by("class", "shopping_cart_badge").get("innerHTML")
		self.assertEqual(items_in_cart, "1")

		bp.navigate_to('https://www.saucedemo.com/cart.html')

		inventory_item_name = bp.element_by("class", "inventory_item_name").get("innerHTML")
		self.assertEqual(item_name, inventory_item_name)

		bp.close()

	def test_javascript_alert(self):
		cf = config.Config()
		cf.http_prefix = 'https://'
		cf.base_url = 'the-internet.herokuapp.com/javascript_alerts'
		cf.options_list.append("headless")
		bp = page.Page(cf)
		bp.go()

		bp.element_by("xpath", "(//button)[1]").click()
		alert = bp.get_alert()

		self.assertEqual(alert.text, "I am a JS Alert")

		alert.accept()
		bp.close()

	def test_javascript_confirm(self):
		cf = config.Config()
		cf.http_prefix = 'https://'
		cf.base_url = 'the-internet.herokuapp.com/javascript_alerts'
		cf.options_list.append("headless")
		bp = page.Page(cf)
		bp.go()

		bp.element_by("xpath", "(//button)[2]").click()
		alert = bp.get_alert()

		self.assertEqual(alert.text, "I am a JS Confirm")

		alert.dismiss()
		bp.close()

	def test_javascript_prompt(self):
		cf = config.Config()
		cf.http_prefix = 'https://'
		cf.base_url = 'the-internet.herokuapp.com/javascript_alerts'
		cf.options_list.append("headless")
		bp = page.Page(cf)
		bp.go()

		bp.element_by("xpath", "(//button)[3]").click()
		alert = bp.get_alert()

		self.assertEqual(alert.text, "I am a JS prompt")

		alert.send_keys("This is a test")
		alert.accept()

		result = bp.element_by("id", "result").get("innerHTML")
		self.assertEqual(result, "You entered: This is a test")

		bp.close()
