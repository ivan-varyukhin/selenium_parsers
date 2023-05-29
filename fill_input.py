import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')
    input_form=browser.find_elements(By.CLASS_NAME, 'form')
    for i in input_form:
        i.send_keys('Text')
    browser.find_element(By.ID, 'btn').click()
    res = browser.find_element(By.ID, 'result').text
    print(res)
    time.sleep(5)