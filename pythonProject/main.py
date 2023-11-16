# Переход к дочерним элементам
# Здесь мы находим все дочерние элементы div с id='parent'.
# //div[@id='parent']/child::*
#
# # Переход к родительскому элементу
# # Этот запрос вернет родительский элемент div с id='child'.
# //div[@id='child']/parent::*
#
# # Переход к следующему соседнему элементу
# # Этот запрос вернет все следующие соседние элементы после div с id='prev_sibling'.
# //div[@id='prev_sibling']/following-sibling::*
#
# # Переход к предыдущему соседнему элементу
# # Этот запрос вернет все предыдущие соседние элементы перед div с id='next_sibling'.
# //div[@id='next_sibling']/preceding-sibling::*
#
# # Переход к конкретному дочернему элементу
# # Этот запрос вернет первый дочерний элемент p у div с id='parent'.
# //div[@id='parent']/child::p[1]
#
# # Поиск по вложенным элементам
# # Этот запрос вернет все элементы span, являющиеся потомками div с id='ancestor'.
# //div[@id='ancestor']//child::span
# Поиск первого дочернего элемента
# Этот запрос вернет первые дочерние элементы для всех div.
# //div/*[1]
#
# # Поиск последнего дочернего элемента
# # Здесь мы находим последние дочерние элементы для всех div.
# //div/*[last()]
#
# # Поиск по порядковому номеру
# # Этот запрос вернет третий элемент li в каждом ul.
# //ul/li[position()=3]
#
# # Поиск элементов, имеющих дочерние элементы
# # Этот запрос вернет все div, которые имеют хотя бы одного потомка.
# //div[count(*) > 0]
#
# # Поиск элементов на определенной глубине
# # Этот запрос вернет все элементы p, находящиеся на четвертом уровне вложенности.
# //*/*/*/*[name()='p']
import requests
from bs4 import BeautifulSoup

url = "https://parsinger.ru/html/mouse/3/3_4.html"
response = requests.get(url)
response.encoding = "utf-8"

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.select("#old_price")

    for p in paragraphs:
        print(p.text)
