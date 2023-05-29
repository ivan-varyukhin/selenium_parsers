from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/draganddrop/1/index.html')
    source_element = browser.find_element(By.ID, "field1")
    target_element = browser.find_element(By.ID, "field2")
    actions = ActionChains(browser)
    actions.drag_and_drop(source_element, target_element).perform()
    print(browser.find_element(By.ID, 'result').text)