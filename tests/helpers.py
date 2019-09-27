from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def evaluate_element_text(element, text):
	WebDriverWait(element.driver, 10).until(ec.text_to_be_present_in_element(element.locator, text))
	return element.text == text
