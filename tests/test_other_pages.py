import unittest
from configs import config
from page import page


class TestOtherPages(unittest.TestCase):
	def test_calculator_page(self):
		cf = config.Config()
		cf.http_prefix = 'http://'
		cf.base_url = 'www.math.com/'
		cf.base_url += 'students/calculators/source/basic.htm'
		cf.options_list.append("headless")
		bp = page.Page(cf)
		bp.go()
		bp.element_by("name", "five").click()
		bp.element_by("name", "plus").click()
		bp.element_by("name", "seven").click()
		bp.element_by("name", "DoIt").click()
		answer = bp.element_by("name", "Input").get("value")
		self.assertEqual(answer, "12")
		bp.close()