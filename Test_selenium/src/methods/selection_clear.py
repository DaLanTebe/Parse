from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as chrome:
    chrome.get('https://parsinger.ru/selenium/5.5/2/1.html')

    elements = chrome.find_elements(By.CLASS_NAME, 'text-field')

    for element in elements:
        if not element.get_attribute('disabled'):
            element.clear()

    chrome.find_element(By.ID, 'checkButton').click()
    time.sleep(5)
