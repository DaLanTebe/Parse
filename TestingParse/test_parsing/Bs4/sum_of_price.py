from bs4 import BeautifulSoup
import requests

url = 'http://parsinger.ru/html/index1_page_1.html'
list = []
first_response = requests.get(url)
first_response.encoding = 'utf-8'

soup = BeautifulSoup(first_response.text, 'html.parser')

nav_menu = [tag.get('href') for tag in soup.find('div', {'class': 'nav_menu'}).find_all('a')]

base_url = 'http://parsinger.ru/html/'

for category in nav_menu:
    request = requests.get(base_url + category)
    request.encoding = 'utf-8'

    soub = BeautifulSoup(request.text, 'html.parser')
    pagen = [tag.get('href') for tag in soub.find('div', {'class', 'pagen'}).find_all('a')]

    for next_url in pagen:
        full_url = base_url + next_url

        pagen_response = requests.get(full_url)
        pagen_response.encoding = 'utf-8'

        beautiful_soup = BeautifulSoup(pagen_response.text, 'html.parser')

        find_all = beautiful_soup.find_all('a', {'class', 'name_item'})

        for current_url in [current_url.get('href') for current_url in find_all]:
            matching_url = base_url + current_url
            current_response = requests.get(matching_url)
            current_response.encoding = 'utf-8'

            matching_soup = BeautifulSoup(current_response.text, 'html.parser')

            price = int(matching_soup.find('span', {'id': 'price'}).text.rstrip(' руб'))
            stock = int(matching_soup.find('span', {'id': 'in_stock'}).text.lstrip('В наличии: '))
            list.append(price * stock)

print(sum(list))
