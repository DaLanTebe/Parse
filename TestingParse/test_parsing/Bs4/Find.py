from bs4 import BeautifulSoup


html_doc = """
<html>
    <head>
        <title>Example Page</title>
    </head>
    <body>
        <div id="main">
            <h1>Hello World</h1>
            <p class="info">This is a paragraph.</p>
            <p class="info">This is another paragraph.</p>
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
            </ul>
        </div>
        <div id="secondary">
            <p>Some additional information.</p>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.find('div', attrs={"id": "main"}))
print(soup.div)
# print(soup.find('p', {'class': 'info'}))

# name - имя тега HTML, который нужно найти. Опциональный параметр.
# attrs - словарь атрибутов и их значений, которые нужно найти. Опциональный параметр.
# text - текст, который нужно найти. Опциональный параметр.
# limit - максимальное количество элементов, которые мы хотим найти. Опциональный параметр.
# recursive - определяет, должны ли мы искать элементы во вложенных тегах. По умолчанию True. Опциональный параметр.
# print(soup.find_all('p', {'class': 'info'}))
