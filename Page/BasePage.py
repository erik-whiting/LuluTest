from selenium import webdriver
from selenium.webdriver.common.by import By
from Page.BaseElement import BaseElement
from selenium.webdriver.chrome.options import Options


class Page:

	def __init__(self, config, url_extension=''):
		self.driver = config.driver
		self.headless = config.headless
		self.full_path_to_driver = config.full_path_to_driver
		self.page = self.web_driver()
		if not url_extension:
			self.url = config.url()
		else:
			self.url = config.url() + '/' + url_extension

	def web_driver(self):
		if self.driver == 'Chrome':
			chrome_options = Options()
			if self.headless:
				chrome_options.add_argument("--headless")
				return webdriver.Chrome(chrome_options=chrome_options)
			if self.full_path_to_driver:
				return webdriver.Chrome(chrome_options=chrome_options, executable_path=self.full_path_to_driver)
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
