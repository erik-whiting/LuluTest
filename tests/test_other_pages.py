import unittest
from configs import config
from page import page


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

		bp.element_by("xpath", "(//button[@class='btn_primary btn_inventory'])[1]").click()
		bp.element_by("xpath", "(//button[@class='btn_primary btn_inventory'])[2]").click()
		bp.element_by("xpath", "(//button[@class='btn_primary btn_inventory'])[3]").click()
		items_in_cart = bp.element_by("class", "shopping_cart_badge").get("innerHTML")
		self.assertEqual(items_in_cart, "3")

		bp.element_by("class", "shopping_cart_link").click()
		bp.element_by("class", "cart_button").click()
		items_in_cart = bp.element_by("class", "shopping_cart_badge").get("innerHTML")
		self.assertEqual(items_in_cart, "2")

		bp.element_by("class", "checkout_button").click()
		bp.element_by("id", "first-name").input_text("Jane")
		bp.element_by("id", "last-name").input_text("Doe")
		bp.element_by("id", "postal-code").input_text("12345")
		bp.element_by("class", "cart_button").click()
		bp.element_by("class", "cart_button").click()
		checkout_complete_page = bp.element_by("class", "complete-header").get("innerHTML")
		self.assertEqual(checkout_complete_page, "THANK YOU FOR YOUR ORDER")

		bp.close()
