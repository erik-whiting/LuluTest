from action.element_actions import ElementActions
from action.page_actions import PageActions
from page_element_interface.IPageElement import *


class Action(PageActions, ElementActions):
    def __init__(self, page):
        self.driver = load_driver()
        PageActions.__init__(self, page, self.driver)
        ElementActions.__init__(self, self.driver)
