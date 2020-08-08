class Step:
    def __init__(self, action_object, operation, subject=None, data=None):
        self.action_object = action_object
        self.operation = operation
        self.subject = subject
        self.data = data
        self.result = None
