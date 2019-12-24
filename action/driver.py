from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Driver:
    def __init__(self, browser_type='chrome', options=None):
        if options is None:
            options = ['headless']

        self.browser = browser_type.lower()
        self.options = options
        if self.browser == 'chrome':
            self.driver = webdriver.Chrome()

    def resolve_options(self, options):
        options_list = webdriver.chrome.options.Options()
        if "headless" in self.options:
            options_list.add_argument('--headless')
        return options_list

    def get_driver(self):
        return self.driver
