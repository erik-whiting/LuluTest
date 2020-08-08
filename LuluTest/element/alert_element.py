from LuluTest.element import BaseElement


class AlertElement(BaseElement):
    def __init__(self, name=''):
        super().__init__(name)
        self.is_alert_element = True
