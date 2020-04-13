from action.element_actions import ElementActions
from action.page_actions import PageActions
from page_element_interface.IPageElement import *


class Action(PageActions, ElementActions):
    def __init__(self, driver_type='Chrome'):
        self.driver = load_driver(driver_type)
        self.action_map = None
        PageActions.__init__(self, self.driver)
        ElementActions.__init__(self, self.driver)
