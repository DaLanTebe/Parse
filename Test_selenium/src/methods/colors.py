from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as chrome:
    chrome.get('https://parsinger.ru/selenium/5.5/4/1.html')

    elements = chrome.find_elements(By.CLASS_NAME, 'parent')

    for element in elements:
        element.find_element(By.CSS_SELECTOR, '[color="blue"]').send_keys(
            element.find_element(By.CSS_SELECTOR, '[color="gray"]').text
        )
        element.find_element(By.CSS_SELECTOR, '[color="gray"]').clear()
        element.find_element(By.TAG_NAME, 'button').click()
    chrome.find_element(By.ID, 'checkAll').click()
    time.sleep(5)

    