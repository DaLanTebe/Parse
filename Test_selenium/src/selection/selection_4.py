from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as chrome:
    chrome.get('http://parsinger.ru/selenium/7/7.html')

    list = []
    elements = chrome.find_elements(By.TAG_NAME, 'option')
    for element in elements:
        list.append(int(element.text))
    chrome.find_element(By.ID, 'input_result').send_keys(sum(list))
    chrome.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(5)