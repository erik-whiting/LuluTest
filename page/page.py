from selenium import webdriver
from selenium.webdriver.common.by import By
from page.base_element import BaseElement
from page.step import Step
from selenium.webdriver.chrome.options import Options
from typing import List, Tuple


class PageBuilder:
	def __init__(self, config, url_extension=''):
		self.driver = config.driver
		self.options_list = config.options_list
		self.page = self.web_driver()
		self.elements = []
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

	def refresh(self):
		self.page.refresh()

	def close(self):
		self.page.close()

	def page_source(self):
		return self.page.page_source

	def get_url(self):
		return self.page.current_url

	def navigate_to(self, url):
		self.page.get(url)

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

	def collect_elements(self, collection_instructions: List[Tuple[str, str]]):
		for collection_instruction in collection_instructions:
			self.elements.append(
				self.element_by(collection_instruction[0], collection_instruction[1])
			)

	@staticmethod
	def do_step(*args):
		# Handle a step object or array
		if len(args) == 2:
			step = Step(args[0], args[1])
		elif len(args) == 3:
			step = Step(args[0], args[1], args[2])
		else:
			step = args[0]

		action = step.action.lower()
		if action == "click":
			step.element.click()
		elif action == "type":
			step.element.input_text(step.data)
		elif action == "clear":
			step.element.clear()
		elif action == "clear text":
			step.element.clear_text()
		elif action == "select":
			step.element.select_drop_down(step.data)

	def do(self, steps):
		if not isinstance(steps, list):
			steps = [steps]
		for step in steps:
			self.do_step(step)
