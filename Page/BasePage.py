from selenium import webdriver
from selenium.webdriver.common.by import By
from Page.BaseElement import BaseElement


class Page:

	def __init__(self, config, url_extension=''):
		self.driver = config.driver
		self.page = self.web_driver()
		if not url_extension:
			self.url = config.url()
		else:
			self.url = config.url() + '/' + url_extension

	def web_driver(self):
		if self.driver == 'Chrome':
			return webdriver.Chrome()
		elif self.driver == 'Safari':
			return webdriver.Safari()

	def go(self):
		self.page.get(self.url)

	def close(self):
		self.page.close()

	def element_by(self, indicator, locator):
		indicator = indicator.lower()
		indicator_converter = {
			"id": By.ID,
			"xpath": By.XPATH,
			"selector": By.CSS_SELECTOR,
			"class": By.CLASS_NAME,
			"link text": By.LINK_TEXT,
			"name": By.NAME,
			"partial link": By.PARTIAL_LINK_TEXT,
			"tag": By.TAG_NAME
		}
		return BaseElement(indicator_converter.get(indicator), locator, self.page)
