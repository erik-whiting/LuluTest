from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def load_element(driver, element):
    until_value = None
    if element.is_page_element:
        until_value = ec.visibility_of_element_located(locator=element.locator)
    elif element.is_alert_element:
        until_value = ec.alert_is_present()
    return WebDriverWait(driver, 10).until(until_value)


def load_driver(browser_type='', options=None):
    if options is None:
        options = ['headless']

    if browser_type == 'Chrome':
        chrome_options = resolve_options(webdriver.chrome.options.Options(), options)
        return webdriver.Chrome(options=chrome_options)
    elif browser_type == 'Safari':
        return webdriver.Safari()


def resolve_options(driver_options, options_list):
    if "headless" in options_list:
        driver_options.add_argument("--headless")
    return driver_options
