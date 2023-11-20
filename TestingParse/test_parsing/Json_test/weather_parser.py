import requests

response = requests.get('https://parsinger.ru/3.4/1/json_weather.json')

list = list(response.json())
date = list[0]['Дата']
temreture = list[0]['Температура воздуха']
for element in response:
    for key, val in element.items():
        if (temreture > val):
            print("sa")
