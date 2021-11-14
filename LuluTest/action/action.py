from LuluTest.action.element_actions import ElementActions
from LuluTest.action.page_actions import PageActions
from LuluTest.action.page_actions_decorator import PageActionsDecorator
from LuluTest.page_element_interface.IPageElement import load_driver


class Action(PageActionsDecorator, ElementActions):
    def __init__(self, browser_options=None):
        self.driver = load_driver(browser_options)
        self.action_map = None
        PageActionsDecorator.__init__(self, PageActions(self.driver))
        ElementActions.__init__(self, self.driver)
