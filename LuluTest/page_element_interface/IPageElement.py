from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from LuluTest.page_element_interface import browser_factory


def load_element(driver, element):
    waiter = None
    if element.is_page_element:
        resolver = get_element_by_resolver(element)
        waiter = ec.visibility_of_element_located(locator=resolver)
    elif element.is_alert_element:
        waiter = ec.alert_is_present()
    return WebDriverWait(driver, 10).until(waiter)


def check_element_text(driver, element, text):
    resolver = get_element_by_resolver(element)
    waiter = ec.text_to_be_present_in_element(locator=resolver, text_=text)
    return WebDriverWait(driver, 10).until(waiter)


def load_driver(browser_type, options=None):
    if options is None:
        options = []
    if 'not headless' not in options:
        options = ['headless']

    return browser_factory.new(browser_type, options)


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
