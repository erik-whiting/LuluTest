from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def load_element(driver, element):
    until_value = None
    if element.is_page_element:
        resolver = get_element_by_resolver(element)
        until_value = ec.visibility_of_element_located(locator=resolver)
    elif element.is_alert_element:
        until_value = ec.alert_is_present()
    return WebDriverWait(driver, 10).until(until_value)


def check_element_text(driver, element, text):
    resolver = get_element_by_resolver(element)
    until_value = ec.text_to_be_present_in_element(locator=resolver, text_=text)
    return WebDriverWait(driver, 10).until(until_value)


def load_driver(browser_type='Chrome', options=None):
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


def get_element_by_resolver(element):
    indicator, value = element.locator
    converter = {
        "id": By.ID,
        "xpath": By.XPATH,
        "selector": By.CSS_SELECTOR,
        "class": By.CLASS_NAME,
        "link text": By.LINK_TEXT,
        "partial link": By.PARTIAL_LINK_TEXT,
        "name": By.NAME,
        "tag": By.TAG_NAME
    }
    by_indicator = converter.get(indicator.lower())
    return by_indicator, value
