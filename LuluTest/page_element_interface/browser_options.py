class BrowserOptions:
    def __init__(self, options_hash=None):
        self.options_hash = options_hash if options_hash else {}
        self.driver_type = self.option_or_default("driver_type", "Chrome")
        self.headless = self.option_or_default("headless", True)
        self.browser_binary_location = self.option_or_default(
            "browser_binary_location", None
        )
        self.webdriver_location = self.option_or_default("webdriver_location", None)
        self.operating_system = self.option_or_default("operating_system", None)

    def option_or_default(self, key, default_value):
        try:
            value = self.options_hash[key]
        except KeyError:
            value = default_value
        return value
