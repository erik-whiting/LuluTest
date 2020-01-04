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
