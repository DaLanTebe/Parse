import requests

first_available_page = None
last_available_page = None
counter = 0

for counter in range(100):

    counter += 1
    url = f'https://parsinger.ru/3.3/4/{counter}.html'

    response = requests.get(url)

    if (response.status_code == 200):
        if (first_available_page == None):
            first_available_page = counter
        last_available_page = counter

print(f"Первая доступная страница: {first_available_page}.html")
print(f"Последняя доступная страница: {last_available_page}.html")
