import unittest

from configs.config import Config
from page.page import Page
from page.step import Step


class TestStep(unittest.TestCase):
    cf = Config()
    cf.http_prefix = 'https://'
    cf.base_url = 'google.com'
    cf.options_list.append("headless")
    step = Step("Type", "in this element", "these words")

    def test_step_creation(self):
        self.assertEqual(self.step.action, "Type")
        self.assertEqual(self.step.element, "in this element")
        self.assertEqual(self.step.data, "these words")

    def test_step_explain(self):
        bp = Page(self.cf)
        bp.go()
        element = bp.element_by("name", "q")
        step_1 = Step("type", element, "This data")
        answer = step_1.explain()
        self.assertEqual(answer, "This step type This data into a input element of name q")
        bp.close()
