import requests
from bs4 import BeautifulSoup
url = "https://parsinger.ru/2.1/DOM/index2.html"
response = requests.get(url)
response.encoding = "utf-8"

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    soup_find = soup.find(id='text777')

    if soup_find:
        find_text = soup_find.text
        print(f"Извлеченный текст: {find_text}")
    else:
        print("Элемент с ID 'text777' не найден.")
else:
    print(f"Не удалось получить доступ к странице, статус-код: {response.status_code}")
