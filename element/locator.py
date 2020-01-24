
class Locator:
    def __init__(self, by, value):
        self.by = by
        self.value = value

    def to_tuple(self):
        return self.by, self.value
