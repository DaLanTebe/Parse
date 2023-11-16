import requests
from bs4 import BeautifulSoup

request = requests.get("https://parsinger.ru/html/mouse/3/3_4.html")
request.encoding = 'utf-8'
soup = BeautifulSoup(request.text, "html.parser")

find_items = soup.select('#old_price')

for find_item in find_items:
    print(find_item)