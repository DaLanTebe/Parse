from bs4 import BeautifulSoup
import requests

base_url = 'https://parsinger.ru/html/index3_page_1.html'

main_list = []

response = requests.get(base_url)

response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')

second_url = [tag.get('href') for tag in soup.find('div', {'class': 'pagen'}).find_all('a')]

for urls in second_url:
    requests_get = requests.get('http://parsinger.ru/html/' + urls)
    requests_get.encoding = 'utf-8'
    beautiful_soup = BeautifulSoup(requests_get.text, 'html.parser')
    list = []
    for elem in beautiful_soup.find_all('a',class_='name_item'):
        list.append(elem.text)
    main_list.append(list)

print(main_list)
