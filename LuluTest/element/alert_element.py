from LuluTest.element import BaseElement


class AlertElement(BaseElement):
    def __init__(self, name=""):
        super().__init__(name)
        self.is_alert_element = True

    @property
    def is_page_element(self):
        return False

    @is_page_element.setter
    def is_page_element(self, *args, **kwargs):
        # This property cannot be changed
        return True

    @property
    def is_alert_element(self):
        return True

    @is_alert_element.setter
    def is_alert_element(self, *args, **kwargs):
        # This property cannot be changed
        return False
