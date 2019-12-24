from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from action.driver import Driver


class ElementActions:
    def __init__(self, driver: Driver):
        self.driver = driver.get_driver()

    def load_element(self, element):
        until_value = None
        if element.is_page_element:
            until_value = ec.visibility_of_element_located(locator=element.locator)
        elif element.is_alert_element:
            until_value = ec.alert_is_present()
        return WebDriverWait(self.driver, 10).until(until_value)

    def click(self, element):
        driver_element = self.load_element(element)
        driver_element.click()

    def input_text(self, element, text):
        driver_element = self.load_element(element)
        driver_element.send_keys(text)

    def clear(self, element):
        driver_element = self.load_element(element)
        driver_element.clear()

    def clear_text(self, element):
        driver_element = self.load_element(element)
        driver_element.send_keys(Keys.CONTROL + 'a')
        driver_element.send_keys(Keys.DELETE)

    def select_drop_down(self, element, index):
        driver_element = self.load_element(element)
        driver_element.select_by_index(index)

    def get_element_attribute(self, element, attribute):
        driver_element = self.load_element(element)
        return driver_element.get_attribute(attribute)

    def get_text(self, element):
        driver_element = self.load_element(element)
        return driver_element.text

    def accept(self, element):
        driver_element = self.load_element(element)
        driver_element.accept()

    def dismiss(self, element):
        driver_element = self.load_element(element)
        driver_element.dismiss()
