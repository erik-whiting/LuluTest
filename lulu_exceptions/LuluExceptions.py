class Error(Exception):
    """Base exception for LuluTest"""
    pass


class PageNotLoadedError(Error):
    """
    When user tries to do driver actions that require a page
    to have been "gone to." We don't want to fail this silently
    to avoid false positives.
    """
    pass


class NoElementWithNameInPage(Error):
    """
    Raise this error when user tries to get element by name
    from a page object, but an element with that name does
    not exist.
    """
    pass


class TooManyElementsWithNameInPage(Error):
    """
    Raise this error when user tries to get element by name
    from a page object, but there are multiple elements with
    that name.
    """
    pass
