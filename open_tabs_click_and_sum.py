from selenium import webdriver
from selenium.webdriver.common.by import By
from math import sqrt

sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html', 'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html',]


with webdriver.Chrome() as browser:
    total=0
    for i in range(len(sites)):
        browser.execute_script(f'window.open("{sites[i]}", "_blank_{i+1}");')
    for x in reversed(range(1,len(browser.window_handles))):
        browser.switch_to.window(browser.window_handles[x])
        browser.find_element(By.CLASS_NAME,'checkbox_class').click()
        total+=sqrt(int(browser.find_element(By.ID, 'result').text))
    print(round(total,9))