
class PageActions:
    def __init__(self, page, driver):
        self.page = page
        self.driver = driver

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
