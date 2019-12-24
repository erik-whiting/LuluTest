from element.base_element import BaseElement


class PageElement(BaseElement):
    def __init__(self, locator, name=''):
        super().__init__(name)
        self.locator = locator.to_tuple()
        self.is_page_element = True
