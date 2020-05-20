class PageActions:
    def __init__(self, driver):
        self.driver = driver
        self.page_loaded = False

    def go(self, page):
        self.driver.get(page.url)

    def go_to(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.close()

    def refresh(self):
        self.driver.refresh()

    def get_page_source(self):
        return self.driver.page_source

    def get_url(self):
        return self.driver.current_url

    def execute_script(self, script):
        return self.driver.execute_script(script)
