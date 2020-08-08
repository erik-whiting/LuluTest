from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from LuluTest.page_element_interface.IPageElement import load_element, check_element_text


class ElementActions:
    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        driver_element = load_element(self.driver, element)
        driver_element.click()

    def input_text(self, element, text):
        driver_element = load_element(self.driver, element)
        driver_element.send_keys(text)

    def clear(self, element):
        driver_element = load_element(self.driver, element)
        driver_element.clear()

    def clear_text(self, element):
        driver_element = load_element(self.driver, element)
        driver_element.send_keys(Keys.CONTROL + 'a')
        driver_element.send_keys(Keys.DELETE)

    def select_drop_down(self, element, visible_text):
        driver_element = load_element(self.driver, element)
        selectable = Select(driver_element)
        selectable.select_by_visible_text(visible_text)

    def upload_file(self, element, path):
        self.input_text(element, path)

    def get_element_attribute(self, element, attribute):
        driver_element = load_element(self.driver, element)
        return driver_element.get_attribute(attribute)

    def get_text(self, element):
        driver_element = load_element(self.driver, element)
        return driver_element.text

    def check_element_text(self, element, text):
        driver_element = check_element_text(self.driver, element, text)
        return driver_element

    def get_attribute(self, element, attribute):
        driver_element = load_element(self.driver, element)
        return driver_element.get_attribute(attribute)

    def accept(self, element):
        driver_element = load_element(self.driver, element)
        driver_element.accept()

    def dismiss(self, element):
        driver_element = load_element(self.driver, element)
        driver_element.dismiss()
