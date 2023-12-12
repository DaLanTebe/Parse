import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()

chrome_options.add_extension('coordinates.crx')

with webdriver.Chrome(options=chrome_options) as browser:
    url = 'https://stepik.org/course/104774'
    browser.get(url)

    time.sleep(10)
