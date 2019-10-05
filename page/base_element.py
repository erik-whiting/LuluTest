from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement:
    def __init__(self, by, value, driver, name=''):
        self.driver = driver
        self.by = by
        self.value = value
        self.name = name
        self.locator = (self.by, self.value)
        self.element = self.web_element()

    def web_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator=self.locator))

    def click(self):
        self.element.click()

    def get(self, attribute):
        return self.element.get_attribute(attribute)

    def input_text(self, text):
        self.element.send_keys(text)

    def clear(self):
        self.element.clear()

    def clear_text(self):
        self.element.send_keys(Keys.CONTROL + 'a')
        self.element.send_keys(Keys.DELETE)

    def select_drop_down(self, index):
        self.element.select_by_index(index)

    @property
    def text(self):
        return self.element.text
