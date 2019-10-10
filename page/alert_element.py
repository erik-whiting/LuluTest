from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from page.base_element import BaseElement


class AlertElement(BaseElement):
    def __init__(self, driver):
        super().__init__(driver)

    def web_element(self):
        return BaseElement.web_element(ec.alert_is_present())

    def accept(self):
        self.activate_element()
        self.element.accept()

    def dismiss(self):
        self.activate_element()
        self.element.dismiss()
