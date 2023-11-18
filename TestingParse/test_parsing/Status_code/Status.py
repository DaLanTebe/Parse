import requests


counter = 0
i = 0
for i in range(200):

    url = f"https://parsinger.ru/3.3/2/{i}.html"

    with requests.Session() as session:
        session_head = session.head(url)
        counter += session_head.status_code
    # response = requests.get(url)
    # response.status_code
    i+= 1
    print(i)

print(counter)