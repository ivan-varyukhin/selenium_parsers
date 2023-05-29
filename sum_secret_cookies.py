from selenium import webdriver

with webdriver.Chrome() as webdriver:
    res = []
    webdriver.get('https://parsinger.ru/methods/3/index.html')
    cookies = webdriver.get_cookies()
    for cookie in cookies:
        res.append(int(cookie['value']))
print(sum(res))