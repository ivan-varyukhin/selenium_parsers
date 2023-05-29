from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


url = 'https://parsinger.ru/draganddrop/2/index.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    main_square = browser.find_element(By.ID,'draggable')
    squares = browser.find_elements(By.CLASS_NAME,'box')
    print(len(squares))
    for square in squares:
        ActionChains(browser).drag_and_drop(main_square,square).perform()
    print(browser.find_element(By.ID,'message').text)