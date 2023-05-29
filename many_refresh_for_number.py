from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/methods/1/index.html')
    while True:
        res = webdriver.find_element(By.ID, 'result').text
        webdriver.refresh()
        if res.isdigit():
            print(res)
            break