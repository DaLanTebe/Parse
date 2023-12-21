from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as chrome:
    chrome.get('https://parsinger.ru/methods/1/index.html')

    while not chrome.find_element(By.ID, 'result').text.isdigit():
        chrome.refresh()
    print(chrome.find_element(By.ID, 'result'))
    time.sleep(5)
