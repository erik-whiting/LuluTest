import unittest
from Configs import Config
from Page import BasePage
from tests import helpers as helper


class TestFeature(unittest.TestCase):
	cf = Config.Config()
	cf.base_url = 'erikwhiting.com'
	cf.subdomain = ''
	cf.base_url += '/newsOutlet'

	def test_write_and_click_with_headless(self):
		self.cf.options_list = ["headless"]
		bp = BasePage.Page(self.cf)
		bp.go()
		bp.element_by("id", "sourceNews").input_text("Hello")
		bp.element_by("id", "transmitter").click()
		english_div = helper.evaluate_element_text(bp.element_by("id", "en1"), "Hello")
		self.assertTrue(english_div)
		bp.close()

	def test_write_and_click_without_headless(self):
		self.cf.options_list = []
		bp = BasePage.Page(self.cf)
		bp.go()
		bp.element_by("id", "sourceNews").input_text("Hello")
		bp.element_by("id", "transmitter").click()
		english_div = helper.evaluate_element_text(bp.element_by("id", "en1"), "Hello")
		self.assertTrue(english_div)
		bp.close()
