from LuluTest.action.element_actions import ElementActions
from LuluTest.action.page_actions import PageActions
from LuluTest.action.page_actions_decorator import PageActionsDecorator
from LuluTest.page_element_interface.IPageElement import load_driver


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
