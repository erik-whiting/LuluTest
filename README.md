# LuluTest
 
LuluTest is an open source testing framework using Python and Selenium.
It is relatively lightweight in that it mostly provides functions and
classes that get pesky things like waits and "find by"s out of the way.

## Basic Usage

LuluTest is designed to be used alone, so there is no need to import
the project into your test harness, although you can if you want.

The framework has three main classes: `Config`, `Page`, and `BaseElement`
that come together to provide you with the ability to robust automated tests. The
basic work flow for creating a test is as such:

* Create a `Config` object
  * This object sets the URL, specific WebDriver, and whether or not
  the driver is headless. You can also optinally set the subdomain and port
  numbers
* Create a `Page` object with the `Config` object
* In your tests, build `BaseElement` objects with the `Page` method `element_by`
and then use the `BaseElement` methods to create your tests.

### Example Usage
Below is an example taken from an early commit of this repository:

```python
import unittest
from Configs import Config
from Page import BasePage
from tests import test_helpers as helper


class TestFeature(unittest.TestCase):
	cf = Config.Config()
	cf.base_url = 'erikwhiting.com'
	cf.subdomain = ''
	cf.base_url += '/newsOutlet'
	bp = BasePage.Page(cf)

	def test_write_and_click(self):
		bp = self.bp
		bp.go()
		bp.element_by("id", "sourceNews").input_text("Hello")
		bp.element_by("id", "transmitter").click()
		english_div = helper.test_element_text(bp.element_by("id", "en1"), "Hello")
		self.assertTrue(english_div)
		bp.close()

```

## Features

There are two main design philosophies driving the development of LuluTest:
1. Hide the tedium and peculiarities inherent in browser automation
from the test scripts themselves, allowing testers to write efficient
and robust tests faster
2. Simplify the test writing process as much as possible allowing non-technical
users to contribute basic test cases while freeing technical
users to focus on more complicated problems.

This philosophies are implemented mostly by keeping the sometimes slow response
time of web elements in mind. The project aims to avoid explicit waits and
sleeps as much as possible.

## Contribution Guide

If you would like to contribute to development, please pull the latest version
of master, create a local branch with a descriptive name, and create a pull
request when you are finished.

Pull requests without tests will most likely be rejected unless the work
you've done is minor enough that a test would be overkill. As of writing
the readme, the project is not big enough to enforce too many more guidelines
than this.

Keep in mind, this framework is designed to be a tool for software
testing and quality assurance, lets practice what we preach.