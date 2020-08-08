from LuluTest.action.page_actions import PageActions
from LuluTest.lulu_exceptions import PageNotLoadedError

'''
This class contains meta-programming to decorate the
PageActions class methods with the necessary pre and
post processing functionality. Proceed with caution.
'''


class PageActionsDecorator(object):
    FUNCTIONS_NEEDING_PAGE_TO_BE_LOADED = [
        'refresh',
        'get_page_source',
        'get_url',
        'execute_script'
    ]

    FUNCTIONS_THAT_LOAD_THE_PAGE = [
        'go',
        'go_to',
        'close'
    ]

    LOAD_WEB_DRIVER_MESSAGE = "Web Driver must go to page " \
                              "before performing this action"

    def __init__(self, model: PageActions):
        self.model = model

    def __getattr__(self, func):
        def method(*args):
            if func in self.FUNCTIONS_NEEDING_PAGE_TO_BE_LOADED:
                return self.check_page_load(func, *args)
            if func in self.FUNCTIONS_THAT_LOAD_THE_PAGE:
                return self.set_page_loaded(func, *args)
        return method

    def check_page_load(self, func, *args):
        if not self.model.page_loaded:
            raise PageNotLoadedError(self.LOAD_WEB_DRIVER_MESSAGE)
        else:
            return getattr(self.model, func)(*args)

    def set_page_loaded(self, func, *args):
        getattr(self.model, func)(*args)
        if func == 'close':
            self.model.page_loaded = False
        else:
            self.model.page_loaded = True
