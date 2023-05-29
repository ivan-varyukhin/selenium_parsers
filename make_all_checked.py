import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/4/4.html')
    [x.click() for x in browser.find_elements(By.CLASS_NAME, 'check')]
    time.sleep(5)