from page import Page
from action.driver import Driver


class PageActions:
    def __init__(self, page: Page, driver: Driver):
        self.page = page
        self.driver = driver.get_driver()

    def go(self):
        self.driver.get(self.page.url)

    def refresh(self):
        self.driver.refresh()

    def close(self):
        self.driver.close()

    def go_to(self, url):
        self.driver.get(url)

    def get_page_source(self):
        return self.driver.page_source

    def get_url(self):
        return self.driver.current_url
