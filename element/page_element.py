from selenium.webdriver.support import expected_conditions as ec
from element.base_element import BaseElement


class PageElement(BaseElement):
    def __init__(self, by, value, driver, name=''):
        super().__init__(driver)
        self.by = by
        self.value = value
        self.name = name
        self.locator = (self.by, self.value)

    def web_element(self):
        return super().web_element(
                ec.visibility_of_element_located(locator=self.locator))

    def select_drop_down(self, index):
        self.activate_element()
        self.element.select_by_index(index)
