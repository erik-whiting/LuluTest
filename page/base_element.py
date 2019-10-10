from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement:
    def __init__(self, driver):
        self.driver = driver
        self.element = None
        self.active_element = False

    def activate_element(self):
        if not self.active_element:
            self.element = self.web_element()
        self.active_element = True

    def deactivate_element(self):
        if self.active_element:
            self.element = None
        self.active_element = False

    def web_element(self, ec):
        return WebDriverWait(self.driver, 10).until(ec)

    def click(self):
        self.activate_element()
        self.element.click()

    def get(self, attribute):
        self.activate_element()
        return self.element.get_attribute(attribute)

    def input_text(self, text):
        self.activate_element()
        self.element.send_keys(text)

    def clear(self):
        self.activate_element()
        self.element.clear()

    def clear_text(self):
        self.activate_element()
        self.element.send_keys(Keys.CONTROL + 'a')
        self.element.send_keys(Keys.DELETE)

    @property
    def text(self):
        self.activate_element()
        return self.element.text
