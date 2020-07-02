from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def new(browser_type, options):
    browser_type = browser_type.lower()
    browser_function = eval('__{}_driver'.format(browser_type))
    return browser_function(options)


def __chrome_driver(options):
    chrome_options = webdriver.chrome.options.Options()
    cdm = ChromeDriverManager().install()
    if 'headless' in options:
        chrome_options.add_argument('--headless')
    return webdriver.Chrome(cdm, options=chrome_options)


def __firefox_driver(options):
    firefox_options = Options()
    gdm = GeckoDriverManager().install()
    if 'headless' in options:
        firefox_options.headless = True
    return webdriver.Firefox(executable_path=gdm, options=firefox_options)
