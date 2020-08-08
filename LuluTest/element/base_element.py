
class BaseElement:
    def __init__(self, name=''):
        self.name = name
        self.active = False
        self.is_page_element = False
        self.is_alert_element = False
