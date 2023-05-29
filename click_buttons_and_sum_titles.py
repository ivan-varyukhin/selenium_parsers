from selenium import webdriver
from selenium.webdriver.common.by import By

k=0
url = 'https://parsinger.ru/blank/3/index.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    all_url = browser.find_elements(By.CLASS_NAME,'buttons')
    for url in all_url:
        url.click()
    for x in browser.window_handles[1:]:
        browser.switch_to.window(x)
        k+=int(browser.title)

print(k)