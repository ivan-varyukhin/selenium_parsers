from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


k = 0

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_3/')

    time.sleep(2)
    for index in range(1, 6):
        div = browser.find_element(
            By.XPATH, f'//*[@id="scroll-container_{index}"]/*')
        while True:
            ActionChains(browser).move_to_element(
                div).scroll_by_amount(1, 500).perform()
            if browser.find_elements(By.XPATH, f"//*[@class='scroll-container_{index}']/*[@class='last-of-list']") != []:
                break
    targets = browser.find_elements(By.TAG_NAME, 'span')
    for target in targets:
        k += int(target.text)

print(k)