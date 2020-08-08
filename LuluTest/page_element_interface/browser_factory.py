from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options


def new(browser_type, options):
    browser_type = browser_type.lower()
    browser_function = eval('__{}_driver'.format(browser_type))
    return browser_function(options)


def __chrome_driver(options):
    chrome_options = webdriver.chrome.options.Options()
    if 'not headless' not in options:
        chrome_options.add_argument('--headless')
    return webdriver.Chrome(options=chrome_options)


def __firefox_driver(options):
    firefox_options = Options()
    if 'not headless' not in options:
        firefox_options.headless = True
    return webdriver.Firefox(options=firefox_options)
