from typing import List, Tuple, Any

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from page.alert_element import AlertElement
from page.base_element import BaseElement
from page.step import Step


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

    def element_by(self, indicator, locator, name=''):
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
        return BaseElement(indicator_converter.get(indicator), locator, self.page, name)

    def element(self, name) -> BaseElement:
        if isinstance(name, str):
            elem = [elem for elem in self.elements if elem[2] == name][0]
        else:
            elem = self.elements[name]
        return self.element_by(elem[0], elem[1])

    def collect_anonymous_element(self, collection_instruction: Tuple[str, str]):
        self.elements.append(
            (collection_instruction[0], collection_instruction[1])
        )

    def collect_named_element(self, collection_instruction: Tuple[str, str, str]):
        self.elements.append(
            (collection_instruction[0], collection_instruction[1], collection_instruction[2])
        )

    def collect_elements(self, collection_instructions: List[Any]):
        for collection_instruction in collection_instructions:
            if len(collection_instruction) == 2:
                self.collect_anonymous_element(collection_instruction)
            elif len(collection_instruction) == 3:
                self.collect_named_element(collection_instruction)

    def get_alert(self):
        return AlertElement(self.page)

    def do_step(self, *args):
        # Handle a step object or array
        if len(args) == 2:
            step = Step(args[0], args[1])
        elif len(args) == 3:
            step = Step(args[0], args[1], args[2])
        else:
            step = args[0]

        if isinstance(step.element, BaseElement):
            element = step.element
        else:
            element = self.resolve_step_element(step.element)

        self.element_action(element, step)

    def resolve_step_element(self, step_element) -> BaseElement:
        if len(step_element) == 2:
            element = self.element_by(
                step_element[0], step_element[1]
            )
        elif len(step_element):
            element = self.element_by(
                step_element[0], step_element[1], step_element[2]
            )
        else:
            element = NotImplementedError
        return element

    @staticmethod
    def element_action(element, step):
        action = step.action.lower()
        if action == "click":
            element.click()
        elif action == "type":
            element.input_text(step.data)
        elif action == "clear":
            element.clear()
        elif action == "clear text":
            element.clear_text()
        elif action == "select":
            element.select_drop_down(step.data)

    def do(self, steps):
        if not isinstance(steps, list):
            steps = [steps]
        for step in steps:
            self.do_step(step)
