from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class AlertElement:
    def __init__(self, driver):
        self.driver = driver
        self.alert = self.alert_element()

    def alert_element(self):
        return WebDriverWait(self.driver, 10).until(ec.alert_is_present())

    def accept(self):
        self.alert.accept()

    def dismiss(self):
        self.alert.dismiss()

    def send_keys(self, text):
        self.alert.send_keys(text)

    @property
    def text(self):
        return self.alert.text
