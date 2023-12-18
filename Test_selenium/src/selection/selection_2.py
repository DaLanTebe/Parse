from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as chrome:
    chrome.get('http://parsinger.ru/selenium/2/2.html')

    chrome.find_element(By.PARTIAL_LINK_TEXT, '16243162441624').click()
    time.sleep(10)