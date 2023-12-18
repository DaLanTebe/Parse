from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as chrome:
    chrome.get('https://parsinger.ru/selenium/1/1.html')

    elements = chrome.find_elements(By.CLASS_NAME, 'form')

    for element in elements:
        element.send_keys('text')

    chrome.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(10)