from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://parsinger.ru/blank/modal/4/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    all_pins = browser.find_elements(By.CLASS_NAME, 'pin')
    for pin in all_pins:
        dg_text = pin.text
        browser.find_element(By.ID, 'check').click()
        prompt = browser.switch_to.alert
        prompt.send_keys(dg_text)
        prompt.accept()
        result = browser.find_element(By.ID, 'result').text
        if result != 'Неверный пин-код':
            print(result)
            break