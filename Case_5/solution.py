import requests
import bs4

url = r'https://obuv-tut2000.ru/magazin/search'
session = requests.Session()


def get_page(query, page: int = 1, timeout=15):
    params = {'p': page, 'gr_smart_search': 1, 'search_text': query}
    resp = session.get(url, params=params, timeout=timeout)
    return resp.url


def sort_key(x):
    return x[1]


search_text = input("Введите запрос: ").strip()
url_new = get_page(search_text)
response = requests.get(url_new)
soup = bs4.BeautifulSoup(response.text, 'html.parser')

items = soup.find_all('form', class_='shop2-product-item product-item')
answ_list = []

for item in items:
    name = item.find('div', class_='gr-product-name')
    price = item.find('div', class_='price-current')
    description = item.find_all('div', class_='option-body')

    key_price = int(price.text.split()[0])

    final_description = [d.text.strip() for d in description]

    answ_list.append((name.text.strip(), key_price, *final_description))
answ_list_sorted = sorted(answ_list, key=sort_key)

with open('answ.csv', 'w', encoding='utf-8') as file:
    for element in answ_list_sorted:
        file.write("; ".join(map(str, element)) + "\n")
