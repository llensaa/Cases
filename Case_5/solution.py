import requests
import bs4
import re
from operator import itemgetter
import csv

url = r'https://obuv-tut2000.ru/'
search_url = url + 'magazin/search'

session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0'}


def get_page(query, page: int = 1, timeout=15):
    '''
    Function, generating search page URL
    :param query: search query
    :param page: page number (default 1)
    :param timeout: request timeout in seconds (default 15)
    :return: URL of the search page
    Note: uses 'a' parameter for page number
    '''
    params = {'a': page, 'gr_smart_search': 1, 'search_text': query}
    resp = session.get(search_url, params=params, timeout=timeout, headers=headers)
    return resp.url


def get_link(item):
    '''
    Function, getting full product URL from product block
    :param item: product block (HTML element)
    :return: full URL of the product
    '''
    name = item.find('div', class_='gr-product-name')
    return url + name.find('a').get('href')


search_text = input("Введите название товара для поиска: ").strip()
url_new = get_page(search_text)
print("URL поиска:", url_new)

response = requests.get(url_new, headers=headers)
soup = bs4.BeautifulSoup(response.text, 'html.parser')

items = soup.find_all('form', class_='shop2-product-item product-item')
answ_list = []
counter = 0

for item in items:
    item_card = requests.get(get_link(item))
    item_card_soup = bs4.BeautifulSoup(item_card.text, 'html.parser')

    name = item.find('div', class_='gr-product-name')
    price = item.find('div', class_='price-current')
    characteristics = item_card_soup.find_all('div', class_='shop2-product-options')

    price_number = int(re.sub(r"\D", "", price.text.strip())) if price else 0

    final_description = []
    for char in characteristics:
        desc = char.find_all('div', class_='option-body')
        final_description.extend([d.text.strip() for d in desc])

    answ_list.append((
        name.text.strip() if name else '', price_number, *final_description))
    counter += 1
    print(f"Карточка {counter} обработана")

answ_list_sorted = sorted(answ_list, key=itemgetter(1), reverse=True)

with open('Cases/Case_5/answ.csv', 'w', encoding='utf-8') as file:
    for row in answ_list_sorted:
        file.write('; '.join([str(e) for e in row]) + '\n')

for element in answ_list_sorted:
    print('; '.join([str(e) for e in element]))
