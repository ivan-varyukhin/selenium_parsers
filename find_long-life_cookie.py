from selenium.webdriver.common.by import By
from selenium import webdriver

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/methods/5/index.html')
    lst_link = [x.get_attribute('href') for x in webdriver.find_elements(By.TAG_NAME, "a")]
    ex, num = 0, 0
    for i in lst_link:
        webdriver.get(i)
        cookies = webdriver.get_cookies()
        if cookies[0]['expiry'] > ex:
            ex = cookies[0]['expiry']
            num = int(webdriver.find_element(By.ID, "result").text)
    print(num)