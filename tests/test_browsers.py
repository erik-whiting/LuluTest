import unittest

from LuluTest.page import Page
from LuluTest.action import Action
from LuluTest.page_element_interface.browser_options import BrowserOptions


class TestBrowsers(unittest.TestCase):
    page = Page("http://erikwhiting.com/newsOutlet")
    actions = None
    import os

    running_in_travis = os.getenv("RUNNING_IN_CI")

    def _set_up(self, browser):
        if self.running_in_travis and browser.lower() == "edge":
            import shutil

            options_hash = BrowserOptions(
                {
                    "driver_type": browser,
                    "headless": True,
                    "browser_binary_location": shutil.which("microsoft-edge-dev"),
                    "webdriver_location": shutil.which("msedgedriver"),
                    "operating_system": "LINUX",
                }
            )
        else:
            options_hash = BrowserOptions({"driver_type": browser})

        self.actions = Action(options_hash)
        self.actions.go(self.page)

    def tearDown(self):
        self.actions.close()
        del self.actions

    def test_page_source_feature_chrome(self):
        self._set_up("Chrome")
        source = self.actions.get_page_source()
        self.assertIn('<body onload="defaultBreaking()">', source)

    def test_page_refresh_chrome(self):
        self._set_up("Chrome")
        self.actions.refresh()
        current_url = self.actions.get_url()
        self.assertEqual("http://erikwhiting.com/newsOutlet/", current_url)

    def test_page_change_url_chrome(self):
        self._set_up("Chrome")
        current_url = self.actions.get_url()
        self.assertEqual("http://erikwhiting.com/newsOutlet/", current_url)

        self.actions.go_to("https://github.com")
        current_url = self.actions.get_url()
        self.assertEqual("https://github.com/", current_url)

    def test_page_source_feature_firefox(self):
        self._set_up("Firefox")
        source = self.actions.get_page_source()
        self.assertIn('<body onload="defaultBreaking()">', source)

    def test_page_refresh_firefox(self):
        self._set_up("Firefox")
        self.actions.refresh()
        current_url = self.actions.get_url()
        self.assertEqual("http://erikwhiting.com/newsOutlet/", current_url)

    def test_page_change_url_firefox(self):
        self._set_up("Firefox")
        current_url = self.actions.get_url()
        self.assertEqual("http://erikwhiting.com/newsOutlet/", current_url)

        self.actions.go_to("https://github.com")
        current_url = self.actions.get_url()
        self.assertEqual("https://github.com/", current_url)

    def test_page_source_feature_edge(self):
        self._set_up("Edge")
        source = self.actions.get_page_source()
        self.assertIn('<body onload="defaultBreaking()">', source)

    def test_page_refresh_edge(self):
        self._set_up("Edge")
        self.actions.refresh()
        current_url = self.actions.get_url()
        self.assertEqual("http://erikwhiting.com/newsOutlet/", current_url)

    def test_page_change_url_edge(self):
        self._set_up("Edge")
        current_url = self.actions.get_url()
        self.assertEqual("http://erikwhiting.com/newsOutlet/", current_url)

        self.actions.go_to("https://github.com")
        current_url = self.actions.get_url()
        self.assertEqual("https://github.com/", current_url)
