from selenium.webdriver.common.by import By
from selenium import webdriver
import time

with webdriver.Chrome() as chrome:
    chrome.get(url='https://nastroyvse.ru/devices/raznoe/na-fleshke-fajlovaya-sistema-ne-raspoznana.html')

    chrome.find_element(By.PARTIAL_LINK_TEXT, 'у флешки файловая система').click()

    time.sleep(10)
