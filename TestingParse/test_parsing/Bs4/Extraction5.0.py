from bs4 import BeautifulSoup
import requests

response = requests.get('http://parsinger.ru/html/hdd/4/4_1.html')

response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')

soup_find_all = soup.find_all('span', ['old_price', 'price'])

price = float(soup.find('span',id='price').text.split()[0])
old_price = float(soup.find('span',id='old_price').text.split()[0])
print(round((old_price - price) * 100 / old_price , 1))