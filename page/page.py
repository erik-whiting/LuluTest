from selenium import webdriver
from selenium.webdriver.common.by import By
from page.base_element import BaseElement
from selenium.webdriver.chrome.options import Options


class PageBuilder:
	def __init__(self, config, url_extension=''):
		self.driver = config.driver
		self.options_list = config.options_list
		self.page = self.web_driver()
		if not url_extension:
			self.url = config.url()
		else:
			self.url = config.url() + '/' + url_extension

	def web_driver(self):
		if self.driver == 'Chrome':
			chrome_options = self.resolve_options(webdriver.chrome.options.Options())
			return webdriver.Chrome(options=chrome_options)
		elif self.driver == 'Safari':
			return webdriver.Safari()

	def resolve_options(self, options):
		if "headless" in self.options_list:
			options.add_argument("--headless")

		return options


class Page(PageBuilder):
	def __init__(self, config, url_extension=''):
		PageBuilder.__init__(self, config, url_extension)

	def go(self):
		self.page.get(self.url)

	def close(self):
		self.page.close()

	def page_source(self):
		return self.page.page_source

	def get_url(self):
		return self.page.current_url

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
