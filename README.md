[![Build Status](https://travis-ci.org/erik-whiting/LuluTest.svg?branch=development)](https://travis-ci.org/erik-whiting/LuluTest)
# LuluTest

## Special Thanks
The following Github users have contributed in some way to LuluTest and I want to thank them so much for their time, effort, and skill.

@benjifs

@alwinaind

@ddrm86

@MarioHdpz

@wangonya

@FarhiaM

@CarolinaKinetic

LuluTest is an open source browser automation framework using Python and Selenium.
It is relatively lightweight in that it mostly provides functions and
classes that get pesky things like waits and "find by"s out of the way.

## Basic Usage

LuluTest is designed to support both white and black box testing. The functions
provided will work as long as the machine running the scripts can access the pages
under test. 

The basic work flow for creating a test is as such:

1. Create a `Page` object with the URL of the page to be tested.
2. Create an `Action` object which will interact with elements
3. Create an `Element` object for each element on the page that will be tested
4. `go` to the page to be tested
5. Create a `Steps` object of actions to take on a page
6. `Do` the `Steps`
7. Do your assertions

### Example Usage
Below is an example test case:

```python
import unittest

from lulu_exceptions import PageNotLoadedError
from page import Page
from element import PageElement
from action import Action
from step import Step, Do, DoStep, Steps


class ExampleTest(unittest.TestCase):
    def test_write_and_click(self):
        page = Page('http://erikwhiting.com/newsOutlet')
        actions = Action()
        page.elements = [
            PageElement(("id", "sourceNews"), "input box"),
            PageElement(("id", "transmitter"), "button"),
            PageElement(("id", "en1"), "english div")
        ]
        actions.go(page)
        actions.input_text(page.get_element("input box"), "Hello")
        actions.click(page.get_element("button"))
        english_div = page.get_element("english div")
        english_text = actions.check_element_text(english_div, "Hello")
        self.assertTrue(english_text)
        actions.close()

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

## LuluTest Architecture

Between December of 2019 and January of 2020, the LuluTest architecture
was redesigned with better principles and implemented in a way as described
in the picture below. If contributing, please do your best to adhere to the
intended arhcitecture.

![LuluTest Architecture](LuluTestArchitecture.PNG)

## Future Work

The ultimate goal of LuluTest is to power a *domain specific language* to help
facilitate communication between business and technical stakeholders about
requirements and testing.

## Contribution Guide

Please see the [Contribution Guide](./CONTRIBUTING.md)

## Set-Up Guide
For setting up a local environment to contribute to testing, please go to the [Set-Up Guide](./SETUP.md)
