import unittest
from page import step


class TestStep(unittest.TestCase):
	step = step.Step("Type", "in this element", "these words")

	def test_step_creation(self):
		self.assertEqual(self.step.action, "Type")
		self.assertEqual(self.step.element, "in this element")
		self.assertEqual(self.step.data, "these words")
