from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.html')
    result=(eval((browser.find_element(By.ID, 'text_box')).text))
    [x.click() for x in browser.find_elements(By.TAG_NAME, 'option') if int(x.text)==result]
    browser.find_element(By.CLASS_NAME, 'btn').click()
    print(browser.find_element(By.ID, 'result').text)