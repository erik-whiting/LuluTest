from .action import Action
from .page_actions import PageActions
from .element_actions import ElementActions

__all__ = [
    'Action',
    'PageActions',
    'ElementActions',
    'page_action_map',
    'element_action_map'
]

page_action_map = {
    "go": PageActions.go,
    "go to": PageActions.go_to,
    "close": PageActions.close,
    "refresh": PageActions.refresh,
    "get source": PageActions.get_page_source,
    "get url": PageActions.get_url
}

element_action_map = {
    "click": ElementActions.click,
    "type": ElementActions.input_text,
    "clear": ElementActions.clear,
    "clear text": ElementActions.clear_text,
    "select": ElementActions.select_drop_down,
    "get attribute": ElementActions.get_element_attribute,
    "check text": ElementActions.check_element_text,
    "accept": ElementActions.accept,
    "dismiss": ElementActions.dismiss
}
