from typing import List, Dict

import yaml
import re

from element import BaseElement, PageElement
from page import Page


def generate_pages(files) -> Dict[str, Page]:
    files = [files] if isinstance(files, str) else files
    pages = {}
    for file in files:
        page_name = re.split('\\\\|/|.yml', file)[-2]
        with open(file) as f:
            page_data = yaml.load(f, Loader=yaml.FullLoader)
        pages[page_name] = generate_page(page_data['page'])
    return pages


def generate_page(page_data) -> Page:
    url = page_data['url']
    page = Page(url)

    elements_data = page_data['elements'] if 'elements' in page_data else []
    page.elements = generate_elements(elements_data)

    return page


def generate_elements(elements_data) -> List[BaseElement]:
    elements = []
    for element_key in elements_data.keys():
        element_data = elements_data[element_key]
        locator = list(element_data)[0]
        locator_val = element_data[locator]
        page_element = PageElement((locator, locator_val), element_key)
        elements.append(page_element)
    return elements
