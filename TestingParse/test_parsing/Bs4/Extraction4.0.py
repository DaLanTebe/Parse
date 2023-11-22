from bs4 import BeautifulSoup
import requests

response = requests.get('https://parsinger.ru/html/index1_page_1.html')

response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')

soup_find_all = soup.find_all('p', {'class': 'price'})

list = []

for tag in soup_find_all:
    text = int(tag.text.rstrip('руб'))
    list.append(text)
print(sum(list))