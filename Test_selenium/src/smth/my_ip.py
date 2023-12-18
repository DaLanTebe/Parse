
from selenium import webdriver
from selenium.webdriver.common.by import By

proxy_list = ['203.142.74.115:8080', '202.154.36.57:8080',
'220.198.112.172:1080', '220.247.165.141:9990',
'213.147.208.35:7788', '202.180.20.66:8080', ]

for PROXY in proxy_list:
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
        url = 'https://2ip.ru/'

        with webdriver.Chrome(options=chrome_options) as browser:
            browser.get(url)
            print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)

            browser.set_page_load_timeout(5)

            proxy_list.remove(PROXY)
    except Exception as _ex:
        print(f"Превышен timeout ожидания для - {PROXY}")
        continue

# import time
# from selenium.webdriver.common.by import By
# from seleniumwire import webdriver
#
# options = {'proxy': {
#     'http': "socks5://D2Frs6:75JjrW@194.28.210.39:9867",
#     'https': "socks5://D2Frs6:75JjrW@194.28.210.39:9867",
#     }}
#
# url = 'https://2ip.ru/'
#
# with webdriver.Chrome(seleniumwire_options=options) as browser:
#     browser.get(url)
#     print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
#     time.sleep(5)