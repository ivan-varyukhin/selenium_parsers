from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


k = 0

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_2/')

    time.sleep(2)
    div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
    while True:
        ActionChains(browser).move_to_element(
            div).scroll_by_amount(1, 500).perform()
        if browser.find_elements(By.CLASS_NAME, 'last-of-list') != []:
            break
    targets = browser.find_element(
        By.ID, 'scroll-container').find_elements(By.TAG_NAME,'p')
    print(targets)
    for target in targets:
        k += int(target.text)
print(k)