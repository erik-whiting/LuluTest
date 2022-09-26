from LuluTest.element import BaseElement


class PageElement(BaseElement):
    def __init__(self, locator, name=""):
        super().__init__(name)
        self.locator = locator

    @property
    def is_page_element(self):
        return True

    @is_page_element.setter
    def is_page_element(self, *args, **kwargs):
        # This property cannot be changed
        return False

    @property
    def is_alert_element(self):
        return False

    @is_alert_element.setter
    def is_alert_element(self, *args, **kwargs):
        # This property cannot be changed
        return False
