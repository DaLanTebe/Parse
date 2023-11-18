import requests



for i in range(1, 201):
    url = f"https://parsinger.ru/3.3/1/{i}.html"

    with requests.Session() as session:
        if (session.head(url).status_code == 200):
            print(session.get(url).text)