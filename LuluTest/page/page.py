from ..lulu_exceptions import *


class Page:
    def __init__(self, url, elements=None):
        if elements is None:
            elements = []
        self.url = url
        self.elements = elements

    def get_element(self, getter):
        element = None
        if isinstance(getter, int):
            element = self.elements[getter]
        elif isinstance(getter, str):
            elements_found_array = [elem for elem in self.elements if elem.name == getter]
            element = self.resolve_found_elements(elements_found_array)
        return element

    @staticmethod
    def resolve_found_elements(elements):
        size = len(elements)
        if size == 1:
            return elements[0]
        elif size == 0:
            raise LuluExceptions.NoElementWithNameInPage
        elif size > 1:
            raise LuluExceptions.TooManyElementsWithNameInPage
