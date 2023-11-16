import requests
from bs4 import BeautifulSoup
url = "https://parsinger.ru/html/hdd/4/4_1.html"
response = requests.get(url)
response.encoding = "utf-8"

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.select("#description > li:nth-child(3)")

    for p in paragraphs:
        print(f'Найденный элемент: {p.text}')
