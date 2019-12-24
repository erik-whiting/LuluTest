from action.element_actions import ElementActions
from action.page_actions import PageActions
from action.driver import Driver


class Action(PageActions, ElementActions):
    def __init__(self, page):
        self.driver = Driver().get_driver()
        PageActions.__init__(self, page, self.driver)
        ElementActions.__init__(self, self.driver)
