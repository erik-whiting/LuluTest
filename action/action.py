from action.element_actions import ElementActions
from action.page_actions import PageActions
from page_element_interface.IPageElement import *
from action.page_actions_decorator import PageActionsDecorator


class Action(PageActionsDecorator, ElementActions):
    def __init__(self, driver_type=None, options=None):
        if driver_type is None:
            driver_type = 'Chrome'
        if options is None:
            options = ['headless']
        self.driver = load_driver(driver_type, options)
        self.action_map = None
        PageActionsDecorator.__init__(self, PageActions(self.driver))
        ElementActions.__init__(self, self.driver)
