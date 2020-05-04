from action.page_actions import PageActions
from lulu_exceptions import PageNotLoadedError

'''
This class contains meta-programming to decorate the
PageActions class methods with the necessary pre and
post processing functionality. Proceed with caution.
'''


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

    def __init__(self, model: PageActions):
        self.model = model

    def __getattr__(self, func):
        def method(*args):
            if func in self.CHECK_PAGE_LOAD:
                return self.check_page_load(func, *args)
            if func in self.SET_PAGE_LOAD:
                return self.set_page_loaded(func, *args)
        return method

    def check_page_load(self, func, *args):
        if not self.model.page_loaded:
            raise PageNotLoadedError("Web Driver must go to page before performing this action")
        else:
            return getattr(self.model, func)(*args)

    def set_page_loaded(self, func, *args):
        getattr(self.model, func)(*args)
        if func == 'close':
            self.model.page_loaded = False
        else:
            self.model.page_loaded = True
