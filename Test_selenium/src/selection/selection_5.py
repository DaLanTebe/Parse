from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as chrome:
    chrome.get('https://parsinger.ru/selenium/6/6.html')
    result = eval(chrome.find_element(By.ID, 'text_box').text)

    chrome.find_element(By.ID, 'selectId').click()
    for element in chrome.find_elements(By.TAG_NAME, 'option'):
        if element.text == str(result):
            element.click()
    chrome.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(5)

