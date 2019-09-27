import unittest
from Configs import Config
from Page import BasePage
from tests import helpers as helper


class TestFeature(unittest.TestCase):
	cf = Config.Config()
	cf.base_url = 'erikwhiting.com'
	cf.subdomain = ''
	cf.base_url += '/newsOutlet'
	bp = BasePage.Page(cf)

	def test_write_and_click(self):
		bp = self.bp
		bp.go()
		bp.element_by("id", "sourceNews").input_text("Hello")
		bp.element_by("id", "transmitter").click()
		english_div = helper.evaluate_element_text(bp.element_by("id", "en1"), "Hello")
		self.assertTrue(english_div)
		bp.close()
