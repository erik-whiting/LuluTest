from LuluTest.element import BaseElement


class PageElement(BaseElement):
    def __init__(self, locator, name=''):
        super().__init__(name)
        self.locator = locator
        self.is_page_element = True
