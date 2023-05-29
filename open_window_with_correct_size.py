from selenium import webdriver
from selenium.webdriver.common.by import By

window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/window_size/2/index.html')
    for x in window_size_x:
        for y in window_size_y:
            browser.set_window_size((x + 16), (y + 133))
            res = browser.find_element(By.ID, 'result').text
            if res != '':
                print(res)
                break