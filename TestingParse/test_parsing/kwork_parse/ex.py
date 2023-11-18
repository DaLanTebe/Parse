import requests
from bs4 import BeautifulSoup

url = "https://kwork.ru/projects"

page_number = 1
search_params = {
    'a': page_number,
}

response = requests.get(url, params=search_params)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    print(response.url)
    selects = soup.select('a')
    for select in selects:
        print(type(select))
        print(str(select.text))
else:
    print("error")
