import urllib3
urllib3.disable_warnings()

from bs4 import BeautifulSoup as bs
import requests


def format_block(obj):
    if obj is None:
        return None
    else:
        return obj.get_text()


def pars_():
    resp = requests.get('https://breffi.ru/ru/about', verify=False)
    if resp.status_code != 200:
        return [('status code error', 'code is not 200'),]
    bs_obj = bs(resp.text, 'html.parser')
    content_section = bs_obj.find('div', {'class': 'content-section worth'})
    if content_section is None:
        return [('content-section worth error', 'content-section worth is not find'),]
    items_obj = content_section.find_all('div', {'content-section__item'})
    resp__ = list()
    if not items_obj:
        return [('content-section__item error', 'content-section__item is not find'),]
    for item in items_obj:
        itemtitle = format_block(
            item.find(
                'div', {
                    'class': 'content-section__itemtitle'}))
        itemtext = format_block(
            item.find(
                'div', {
                    'class': 'content-section__itemtext'}))
        resp__.append((itemtitle, itemtext))
    return resp__


if __name__ == '__main__':
    result = pars_()
    [print(f'{item[0]}:\n{item[1]}\n') for item in result]
