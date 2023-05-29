from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://parsinger.ru/blank/modal/2/index.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    all_buttons = browser.find_elements(By.CLASS_NAME, 'buttons')
    for button in all_buttons:
        button.click()
        browser._switch_to.alert.accept()
        if browser.find_element(By.ID, 'result').text:
            print(browser.find_element(By.ID, 'result').text)
            break