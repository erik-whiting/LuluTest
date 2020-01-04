from lulu_exceptions import *


class PageActions:
    def __init__(self, driver):
        self.driver = driver
        self.page_loaded = False

    def go(self, page):
        self.driver.get(page.url)
        self.page_loaded = True

    def go_to(self, url):
        self.driver.get(url)
        self.page_loaded = True

    def close(self):
        self.driver.close()
        self.page_loaded = False

    def refresh(self):
        self.__check_page_load()
        self.driver.refresh()

    def get_page_source(self):
        self.__check_page_load()
        return self.driver.page_source

    def get_url(self):
        self.__check_page_load()
        return self.driver.current_url

    def __check_page_load(self):
        if not self.page_loaded:
            raise PageNotLoadedError("Web Driver must go to page before performing this action")
