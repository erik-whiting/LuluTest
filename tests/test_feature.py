import unittest
from configs import config
from page import page, step
from tests import helpers as helper


class TestFeature(unittest.TestCase):
	cf = config.Config()
	cf.base_url = 'erikwhiting.com'
	cf.subdomain = ''
	cf.base_url += '/newsOutlet'

	def test_write_and_click_with_headless(self):
		self.cf.options_list = ["headless"]
		bp = page.Page(self.cf)
		bp.go()
		bp.element_by("id", "sourceNews").input_text("Hello")
		bp.element_by("id", "transmitter").click()
		english_div = helper.evaluate_element_text(bp.element_by("id", "en1"), "Hello")
		self.assertTrue(english_div)
		bp.close()

	def test_page_source_feature(self):
		self.cf.options_list = ["headless"]
		bp = page.Page(self.cf)
		bp.go()
		source = bp.page_source()
		self.assertIn('<body onload="defaultBreaking()">', source)

	def test_page_url(self):
		self.cf.options_list = ["headless"]
		bp = page.Page(self.cf)
		bp.go()
		current_url = bp.get_url()
		if current_url[current_url.__len__()-1] == "/":
			current_url = current_url[:-1]
		self.assertEqual(self.cf.url(), current_url)

	def test_page_refresh(self):
		self.cf.options_list = ["headless"]
		bp = page.Page(self.cf)
		bp.go()

		bp.refresh()
		current_url = bp.get_url()
		if current_url[current_url.__len__()-1] == "/":
			current_url = current_url[:-1]
		self.assertEqual(self.cf.url(), current_url)

	def test_page_change_url(self):
		self.cf.options_list = ["headless"]
		bp = page.Page(self.cf)
		bp.go()

		current_url = bp.get_url()
		if current_url[current_url.__len__()-1] == "/":
			current_url = current_url[:-1]
		self.assertEqual(self.cf.url(), current_url)

		bp.navigate_to('https://github.com')
		current_url = bp.get_url()
		if current_url[current_url.__len__()-1] == "/":
			current_url = current_url[:-1]
		self.assertEqual('https://github.com', current_url)

	def test_do_step(self):
		self.cf.options_list.append("headless")
		bp = page.Page(self.cf)
		bp.go()
		input_element = bp.element_by("id", "sourceNews")
		transmit_button = bp.element_by("id", "transmitter")
		bp.do_step("type", input_element, "Hello")
		bp.do_step("click", transmit_button)
		english_div = helper.evaluate_element_text(bp.element_by("id", "en1"), "Hello")
		self.assertTrue(english_div)

	def test_do(self):
		self.cf.options_list.append("headless")
		bp = page.Page(self.cf)
		bp.go()
		input_element = bp.element_by("id", "sourceNews")
		transmit_button = bp.element_by("id", "transmitter")
		steps = [
			step.Step("type", input_element, "Hello"),
			step.Step("click", transmit_button)
		]
		bp.do(steps)
		english_div = helper.evaluate_element_text(bp.element_by("id", "en1"), "Hello")
		self.assertTrue(english_div)

	def test_element_collection_and_steps(self):
		self.cf.options_list.append("headless")
		bp = page.Page(self.cf)
		bp.go()
		bp.collect_elements([
			("id", "sourceNews"),
			("id", "transmitter")
		])
		steps = [
			step.Step("type", bp.elements[0], "Hello"),
			step.Step("click", bp.elements[1])
		]
		bp.do(steps)
		english_div = helper.evaluate_element_text(bp.element_by("id", "en1"), "Hello")
		self.assertTrue(english_div)

	def test_named_elements(self):
		self.cf.options_list.append("headless")
		bp = page.Page(self.cf)
		bp.go()
		bp.collect_elements([
			("id", "sourceNews", "input"),
			("id", "transmitter", "button")
		])
		steps = [
			step.Step("type", bp.element("input"), "Hello"),
			step.Step("click", bp.element("button"))
		]
		bp.do(steps)
		english_div = helper.evaluate_element_text(bp.element_by("id", "en1"), "Hello")
		self.assertTrue(english_div)

