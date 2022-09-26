import unittest

from LuluTest.page_element_interface.browser_options import BrowserOptions


class MyTestCase(unittest.TestCase):
    def test_default_values(self):
        options = BrowserOptions()
        self.assertEqual(options.driver_type, "Chrome")
        self.assertTrue(options.headless)
        self.assertIsNone(options.browser_binary_location)
        self.assertIsNone(options.webdriver_location)
        self.assertIsNone(options.operating_system)

    def test_setting_one_value(self):
        options = BrowserOptions({"driver_type": "Firefox"})
        self.assertEqual(options.driver_type, "Firefox")
        self.assertTrue(options.headless)
        self.assertIsNone(options.browser_binary_location)
        self.assertIsNone(options.webdriver_location)
        self.assertIsNone(options.operating_system)

    def test_setting_all_values(self):
        driver_type = "Firefox"
        headless = False
        browser_location = "/usr/bin/browser"
        driver_location = "/usr/bin/driver"
        operating_system = "LINUX"
        options = BrowserOptions(
            {
                "driver_type": driver_type,
                "headless": headless,
                "browser_binary_location": browser_location,
                "webdriver_location": driver_location,
                "operating_system": operating_system,
            }
        )
        self.assertEqual(options.driver_type, driver_type)
        self.assertFalse(options.headless)
        self.assertEqual(options.browser_binary_location, browser_location)
        self.assertEqual(options.webdriver_location, driver_location)
        self.assertEqual(options.operating_system, operating_system)
