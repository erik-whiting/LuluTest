import unittest

from LuluTest import *


class SmokeTest(unittest.TestCase):
    def test_smoke_test(self):
        erik_whiting = Page('http://erikwhiting.com')
        link = PageElement(('Link Text', 'blog'), 'blog link')
        actions = Action()
        actions.go(erik_whiting)
        actions.click(link)
        url = actions.get_url()
        self.assertEqual(url, 'https://blog.erikwhiting.com/')

    def test_page_not_loaded_exception(self):
        actions = Action()
        self.assertRaises(PageNotLoadedError, actions.get_url)

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

    def test_step(self):
        erik_whiting = Page('http://erikwhiting.com')
        actions = Action()
        erik_whiting.elements = [
            PageElement(("Link Text", "blog"), "blog link")
        ]
        actions.go(erik_whiting)
        step1 = Step(actions, "click", erik_whiting.get_element("blog link"))
        DoStep(step1)
        url = actions.get_url()
        self.assertEqual(url, 'https://blog.erikwhiting.com/')
        actions.close()

    def test_steps(self):
        actions = Action()
        news_site = Page('http://erikwhiting.com/newsOutlet')
        news_site.elements = [
            PageElement(("id", "sourceNews"), "input box"),
            PageElement(("id", "transmitter"), "button"),
            PageElement(("id", "en1"), "english div")
        ]
        actions.go(news_site)
        steps = Steps(actions, [
            ('type', news_site.get_element('input box'), 'Hello'),
            ('click', news_site.get_element('button'))
        ])
        Do(steps)
        english_text = actions.check_element_text(news_site.get_element('english div'), "Hello")
        self.assertTrue(english_text)
        actions.close()
