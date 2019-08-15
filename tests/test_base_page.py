import unittest
from Configs import Config
from Page import BasePage


class TestBasePage(unittest.TestCase):
	cf = Config.Config()
	cf.driver = 'TestDriver'
	cf.base_url = 'TestMe.com'

	def test_base_page_returns_config_url(self):
		bp = BasePage.Page(self.cf)
		self.assertEqual(bp.url, self.cf.url())

	def test_bast_page_returns_config_url_with_sub_dir(self):
		bp = BasePage.Page(self.cf, 'about')
		self.assertEqual(bp.url, self.cf.url() + '/about')
