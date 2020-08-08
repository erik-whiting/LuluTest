from typing import List, Dict

import yaml
import re
import json

from LuluTest.element import BaseElement, PageElement
from LuluTest.page import Page


def generate_pages(files) -> Dict[str, Page]:
    files = [files] if isinstance(files, str) else files
    pages = {}
    for file in files:
        page_name = re.split('\\\\|/|\.', file)[-2]
        pages[page_name] = generate_page(file)
    return pages


def generate_page(file) -> Page:
    file_type = file.split('.')[-1]
    file_type = file_type.lower()
    gen_function = eval('generate_page_from_{}'.format(file_type))
    page = gen_function(file)
    return page


def generate_page_from_yml(file) -> Page:
    with open(file) as f:
        page_data = yaml.load(f, Loader=yaml.FullLoader)['page']
    url = page_data['url']
    page = Page(url)

    elements_data = page_data['elements'] if 'elements' in page_data else []
    page.elements = generate_elements(elements_data)

    return page


def generate_page_from_json(file) -> Page:
    with open(file) as file:
        page_data = json.load(file)['page']
    url = page_data['url']
    page = Page(url)
    json_elements = page_data['elements']
    element_dict = {}
    for je in json_elements:
        locator_dict = {je['locator']: je['value']}
        name = je['name']
        element_dict[name] = locator_dict
    page.elements = generate_elements(element_dict)
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
