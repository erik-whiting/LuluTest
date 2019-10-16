[![Build Status](https://travis-ci.org/erik-whiting/LuluTest.svg?branch=development)](https://travis-ci.org/erik-whiting/LuluTest)
# LuluTest

LuluTest is an open source testing framework using Python and Selenium.
It is relatively lightweight in that it mostly provides functions and
classes that get pesky things like waits and "find by"s out of the way.

## Basic Usage

LuluTest is designed to be used alone, so there is no need to import
the project into your test harness, although you can if you want.

The framework has three main classes: `Config`, `Page`, and `BaseElement`
that come together to provide you with the ability to produce robust automated tests. The
basic work flow for creating a test is as such:

* Create a `Config` object
  * This object sets the URL, specific WebDriver, and whether or not
  the driver is headless. You can also optinally set the subdomain and port
  numbers of the URL
* Create a `Page` object with the `Config` object
* In your tests, you can either use the Page object to manipulate webpages, or use the step class

### Example Usage
Below is an example test case:

```python
import unittest
from configs import config
from page import page
from tests import helpers as helper


class TestFeature(unittest.TestCase):
    cf = config.Config()
    cf.base_url = 'erikwhiting.com'
    cf.subdomain = ''
    cf.base_url += '/newsOutlet'
    cf.options_list.append("headless")
    bp = None
    
    @classmethod
    def setUp(cls):
        cls.bp = Page(cls.cf)
        cls.bp.go()
    
    @classmethod
    def tearDown(cls):
        cls.bp.close()

    # Same kind of test but with the do method
    def test_write_and_click_with_headless(self):
        self.bp.collect_elements([
            ("id", "sourceNews", "input box"),
            ("id", "transmitter", "button"),
            ("id", "en1", "english div")
        ])
        self.bp.element("input box").input_text("Hello")
        self.bp.element("button").click()
        english_div = helper.evaluate_element_text(self.bp.element("english div"), "Hello")
        self.assertTrue(english_div)
    
        def test_do(self):
        self.bp.collect_elements([
            ("id", "sourceNews"),
            ("id", "transmitter")
        ])
        input_element = self.bp.elements[0]
        transmit_button = self.bp.elements[1]
        steps = [
            Step("type", input_element, "Hello"),
            Step("click", transmit_button)
        ]
        self.bp.do(steps)
        english_div = helper.evaluate_element_text(
            self.bp.grab("id", "en1"),
            "Hello"
        )
        self.assertTrue(english_div)

```

## Features

There are two main design philosophies driving the development of LuluTest:

1. Hide the tedium and peculiarities inherent in browser automation
from the test scripts themselves, allowing testers to write efficient
and robust tests faster

2. Simplify the test writing process as much as possible so non-technical
users can contribute basic test cases while freeing technical
users to focus on more technically complex issues.

These philosophies are implemented mostly by keeping the sometimes slow
response time of web elements in mind. The project aims to avoid
explicit waits and sleeps as much as possible.

## Future Work

The ultimate goal of LuluTest is to become a *domain specific language* for
testing that could be further implemented and extended with other DSLs to
create a medium of communication for developers and domain experts.

## Contribution Guide

Please see the [Contribution Guide](./CONTRIBUTING.md)

## Set-Up Guide
For setting up a local environment to contribute to testing, please go to the [Set-Up Guide](./SETUP.md)
