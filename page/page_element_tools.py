from selenium.webdriver.common.by import By

from element.alert_element import AlertElement
from element.page_element import PageElement


class ElementTools:
    @staticmethod
    def get_page_element(page, indicator: str, locator: str, name='') -> PageElement:
        indicator = indicator.lower()
        converter = {
            "id": By.ID,
            "xpath": By.XPATH,
            "selector": By.CSS_SELECTOR,
            "class": By.CLASS_NAME,
            "link text": By.LINK_TEXT,
            "name": By.NAME,
            "partial link": By.PARTIAL_LINK_TEXT,
            "tag": By.TAG_NAME
        }
        return PageElement(converter.get(indicator), locator, page, name)

    @staticmethod
    def get_alert_element(page):
        return AlertElement(page)


