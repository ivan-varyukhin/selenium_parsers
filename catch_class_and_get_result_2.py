from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

url = 'http://parsinger.ru/expectations/6/index.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
    elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'Y1DM2GR')))
    print(elem.text)