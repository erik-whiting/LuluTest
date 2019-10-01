import unittest
from configs import config
from page import page


class TestBasePage(unittest.TestCase):
	cf = config.Config()
	cf.driver = 'TestDriver'
	cf.base_url = 'TestMe.com'

	def test_base_page_returns_config_url(self):
		bp = page.Page(self.cf)
		self.assertEqual(bp.url, self.cf.url())

	def test_base_page_returns_config_url_with_sub_dir(self):
		bp = page.Page(self.cf, 'about')
		self.assertEqual(bp.url, self.cf.url() + '/about')

	def test_page_knows_its_headless(self):
		self.cf.options_list = ['headless']
		bp = page.Page(self.cf)
		self.assertIn("headless", bp.options_list)

	def test_page_knows_its_not_headless(self):
		self.cf.options_list = []
		bp = page.Page(self.cf)
		self.assertNotIn("headless", bp.options_list)