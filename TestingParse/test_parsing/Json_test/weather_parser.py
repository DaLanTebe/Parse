import requests

response = requests.get('https://parsinger.ru/3.4/1/json_weather.json')

list = list(response.json())

lambda x: filter(x['Температура воздуха'] - 1, list)