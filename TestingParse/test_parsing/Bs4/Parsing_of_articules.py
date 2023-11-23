from bs4 import BeautifulSoup
import requests

url = 'https://parsinger.ru/html/index3_page_1.html'

response = requests.get(url)

response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')

find_all = soup.find('div', class_='pagen').find_all('a')
list = []
base_url = 'https://parsinger.ru/html/'
for tag in find_all:
    new_url = base_url + tag.get('href')
    new_response = requests.get(new_url)
    new_response.encoding = 'utf-8'
    beautiful_soup = BeautifulSoup(new_response.text, 'html.parser')
    for element in beautiful_soup.find_all('a', class_='name_item'):
        get = requests.get(base_url + element.get('href'))
        get.encoding = 'utf-8'
        soub = BeautifulSoup(get.text, 'html.parser')
        list.append(int(soub.find('p', class_='article').text.lstrip('Артикул: ')))

print(sum(list))