from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

result = []

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/3/')

    tag_input = browser.find_elements(By.TAG_NAME, 'input')
    tag_span = browser.find_elements(By.TAG_NAME, 'span')

    for ti, ts in zip(tag_input, tag_span):
        ti.send_keys(Keys.DOWN)
        ti.click()
        if ts.text:
            result.append(int(ti.get_attribute('id')))

print(sum(result))