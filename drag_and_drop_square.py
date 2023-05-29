from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


url = 'https://parsinger.ru/draganddrop/3/index.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    main_square = browser.find_element(By.ID,'block1')
    for _ in range(5):
        ActionChains(browser).click_and_hold(main_square).move_by_offset(50,0).perform()
    main_square.click()
    print(browser.find_element(By.ID,'message').text)