class OldStep:
    def __init__(self, action, element, data=''):
        self.action = action
        self.element = element
        self.data = data
        self.tag_name = ''

    def tag_name_setter(self):
        if isinstance(type(self.element), str):
            self.tag_name = ''
        else:
            self.element.activate_element()
            self.tag_name = self.element.element.tag_name

    def explain(self):
        self.tag_name_setter()
        return str(
            "This step {0} {1} into a {2} element of {3} {4}".format(
                self.action,
                self.data,
                self.tag_name,
                self.element.by,
                self.element.value
            )
        )
