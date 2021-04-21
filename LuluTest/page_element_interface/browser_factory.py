from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import webdriver as EdgeDriver

from LuluTest.page_element_interface.browser_options import BrowserOptions


def new(browser_options: BrowserOptions):
    browser_type = browser_options.driver_type.lower()
    browser_function = eval('__{}_driver'.format(browser_type))
    return browser_function(browser_options)


def __chrome_driver(browser_options):
    chrome_options = webdriver.chrome.options.Options()
    if browser_options.headless:
        chrome_options.add_argument('--headless')
    return webdriver.Chrome(options=chrome_options)


def __firefox_driver(browser_options):
    firefox_options = Options()
    if browser_options.headless:
        firefox_options.headless = True
    return webdriver.Firefox(options=firefox_options)


def __edge_driver(browser_options):
    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    if browser_options.headless:
        edge_options.add_argument('headless')
    return EdgeDriver.WebDriver(options=edge_options)
