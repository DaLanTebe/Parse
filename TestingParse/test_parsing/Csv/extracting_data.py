import requests
import csv
from bs4 import BeautifulSoup

base_url = 'https://parsinger.ru/html/'

with open("result.csv", 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость', 'Объем буферной памяти', 'Цена'])

    url = 'https://parsinger.ru/html/index4_page_1.html'

    response = requests.get(url)
    response.encoding = 'utf-8'

    category_pagen = BeautifulSoup(response.text, 'html.parser')

    category_urls = category_pagen.find('div', 'nav_menu').find_all('a')

    for category_url in category_urls:

        category = base_url + category_url.get('href')

        resp = requests.get(category)
        resp.encoding = 'utf-8'

        cat = BeautifulSoup(resp.text, 'html.parser')

        pagen = cat.find('div', 'pagen').find_all("a")

        for page in pagen:

            full_url = base_url + page.get('href')

            result_response = requests.get(url)
            result_response.encoding = 'utf-8'

            extract = BeautifulSoup(result_response.text, 'html.parser')

            names = [name.text.strip() for name in extract.find_all('div', 'name_item')]

            brands = [brand.text.strip() for brand in extract.find_all('div', 'name_item')]
            names = [name.text.strip() for name in extract.find_all('div', 'name_item')]
            names = [name.text.strip() for name in extract.find_all('div', 'name_item')]
            names = [name.text.strip() for name in extract.find_all('div', 'name_item')]
