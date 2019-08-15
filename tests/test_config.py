import unittest
from Configs import Config


class TestConfigs(unittest.TestCase):

	test_url = 'eriktest.com'
	test_sub_domain = 'test'
	test_port = '5000'

	def test_config_returns_basic_url(self):
		cf = Config.Config()
		cf.base_url = self.test_url
		cf.subdomain = ''
		cf.port = ''
		self.assertEqual(cf.url(), 'http://' + self.test_url)

	def test_config_returns_url_with_subdomain(self):
		cf = Config.Config()
		cf.base_url = self.test_url
		cf.subdomain = self.test_sub_domain
		cf.port = ''
		self.assertEqual(cf.url(), 'http://' + self.test_sub_domain + '.' + self.test_url)

	def test_config_returns_url_with_port_only(self):
		cf = Config.Config()
		cf.base_url = self.test_url
		cf.subdomain = ''
		cf.port = self.test_port
		self.assertEqual(cf.url(), 'http://' + self.test_url + ':' + self.test_port)

	def test_config_returns_url_with_port_and_subdomain(self):
		cf = Config.Config()
		cf.base_url = self.test_url
		cf.subdomain = self.test_sub_domain
		cf.port = self.test_port
		val_to_test = 'http://' + self.test_sub_domain + '.' + self.test_url + ':' + self.test_port
		self.assertEqual(cf.url(), val_to_test)
