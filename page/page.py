from typing import List, Tuple, Any

from selenium.webdriver.common.by import By

from page.page_builder import PageBuilder
from element.base_element import BaseElement
from element.alert_element import AlertElement
from element.page_element import PageElement
from step.step import Step


class Page(PageBuilder):
    def __init__(self, config):
        PageBuilder.__init__(self, config)

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

    def element(self, name) -> BaseElement:
        if isinstance(name, str):
            elem = [elem for elem in self.elements if elem[2] == name][0]
        else:
            elem = self.elements[name]
        return self.element_tools.get_page_element(self.page, elem[0], elem[1])

    def grab(self, by, locator):
        # For grabbing one element on page
        # Use element collection when multiple
        # elements are to be used.
        return self.element_tools.get_page_element(self.page, by, locator)

    # Factory method
    def collect_elements(self, collection_instructions: List[Any]):
        for collection_instruction in collection_instructions:
            if len(collection_instruction) == 2:
                self.collect_anonymous_element(collection_instruction)
            elif len(collection_instruction) == 3:
                self.collect_named_element(collection_instruction)

    def collect_anonymous_element(self, collection_instruction: Tuple[str, str]):
        self.elements.append(
            (collection_instruction[0], collection_instruction[1])
        )

    def collect_named_element(self, collection_instruction: Tuple[str, str, str]):
        self.elements.append(
            (collection_instruction[0],
             collection_instruction[1],
             collection_instruction[2])
        )

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

        if isinstance(step.element, PageElement):
            element = step.element
        else:
            element = self.resolve_step_element(step.element)

        self.element_tools.element_action(element, step)

    def resolve_step_element(self, step_element) -> PageElement:
        if len(step_element) == 2:
            element = self.element_tools.get_page_element(
                self.page, step_element[0], step_element[1]
            )
        elif len(step_element):
            element = self.element_tools.get_page_element(
                self.page, step_element[0], step_element[1], step_element[2]
            )
        else:
            element = NotImplementedError
        return element

    def do(self, steps):
        if not isinstance(steps, list):
            steps = [steps]
        for step in steps:
            self.do_step(step)
