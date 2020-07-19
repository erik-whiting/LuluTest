from action.element_actions import ElementActions
from action.page_actions import PageActions
from page_element_interface.IPageElement import *
from action.page_actions_decorator import PageActionsDecorator


class Action(PageActionsDecorator, ElementActions):
    def __init__(self, driver_type='Chrome'):
        self.driver = load_driver(driver_type)
        self.action_map = None
        PageActionsDecorator.__init__(self, PageActions(self.driver))
        ElementActions.__init__(self, self.driver)
