from urllib.parse import urlparse


class PageConfig:
    base_url = ''
    http_prefix = 'http://'

    def __init__(self, url, driver='Chrome'):
        # Set your configuration items here
        self.driver = driver
        self.parse_url(url)
        # Example: self.options_list = ["headless"]
        self.options_list = []

    def parse_url(self, url):
        parsed_url = urlparse(url)
        if parsed_url.scheme == '':
            self.http()
        else:
            self.http_prefix = parsed_url.scheme + "://"

        if parsed_url.netloc == '':
            self.base_url = parsed_url.path
        else:
            self.base_url = parsed_url.netloc + parsed_url.path

    def http(self):
        self.http_prefix = 'http://'

    def https(self):
        self.http_prefix = 'https://'

    def set_driver(self, driver):
        self.driver = driver

    def url(self):
        full_url = self.base_url
        full_url = self.http_prefix + full_url
        return full_url
