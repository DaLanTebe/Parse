from bs4 import BeautifulSoup
import lxml
import requests
import re

result = 0

response = requests.get('https://parsinger.ru/4.3/2/index.html')

response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'lxml')

articuls = soup.find_all('p', {"class": "card-articul"})

num = [int(e) for e in re.findall(r'-?\d+\.?\d*', str(articuls))]

print(sum(num))