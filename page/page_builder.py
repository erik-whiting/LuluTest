from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from page.page_element_tools import ElementTools


class PageBuilder:
    def __init__(self, config, url_extension=''):
        self.driver = config.driver
        self.options_list = config.options_list
        self.page = self.web_driver()
        self.elements = []
        self.element_tools = ElementTools()
        if not url_extension:
            self.url = config.url()
        else:
            self.url = config.url() + '/' + url_extension

    def web_driver(self):
        if self.driver == 'Chrome':
            chrome_options = self\
                .resolve_options(webdriver.chrome.options.Options())
            return webdriver.Chrome(options=chrome_options)
        elif self.driver == 'Safari':
            return webdriver.Safari()

    def resolve_options(self, options):
        if "headless" in self.options_list:
            options.add_argument("--headless")

        return options
