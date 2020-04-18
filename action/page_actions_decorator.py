from action.page_actions import PageActions
from lulu_exceptions import PageNotLoadedError


class PageActionsDecorator(object):
    CHECK_PAGE_LOAD = [
        'refresh',
        'get_page_source',
        'get_url'
    ]

    SET_PAGE_LOAD = [
        'go',
        'go_to',
        'close'
    ]

    def __init__(self, page_actions: PageActions):
        self.model = page_actions

    def __getattr__(self, item):
        func = getattr(self.model, item)
        if item in self.CHECK_PAGE_LOAD:
            self.check_page_load(func)
        elif item in self.SET_PAGE_LOAD:
            self.set_page_loaded(func)

    def check_page_load(self, func):
        if not self.model.page_loaded:
            raise PageNotLoadedError("Web Driver must go to page before performing this action")
        else:
            func()

    def set_page_loaded(self, func):
        func()
        if func.__name__ == 'close':
            self.model.page_loaded = False
        else:
            self.model.page_loaded = True
