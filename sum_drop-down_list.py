import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/7/7.html')
    sum_opt = sum([int(i.text) for i in browser.find_elements(By.TAG_NAME, 'option')])
    browser.find_element(By.ID, 'input_result').send_keys(sum_opt)
    browser.find_element(By.ID, 'sendbutton').click()
    print(browser.find_element(By.ID, 'result').text)
    time.sleep(10)