from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as chrome:
    chrome.get('https://parsinger.ru/selenium/5.5/3/1.html')

    elements = chrome.find_elements(By.CLASS_NAME, 'parent')

    list = []
    for element in elements:
        if not element.is_selected():
            list.append(int(element.text))

    print(sum(list))