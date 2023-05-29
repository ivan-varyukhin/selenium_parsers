from selenium import webdriver
from selenium.webdriver.common.by import By

size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/window_size/2/index.html')
    for x in size_x:
        for y in size_y:
            browser.set_window_size(x + 16, y + 133)
            if browser.find_element(By.ID, 'result').text:
                print(browser.get_window_size())
                browser.quit()