
class Page:
    def __init__(self, url, elements=None):
        if elements is None:
            elements = []
        self.url = url
        self.elements = elements

