import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from browser_setup import browser

data = []
count = []
with browser:
    browser.get('https://parsinger.ru/infiniti_scroll_1/')
    time.sleep(1)

    flag = True
    while flag:
        element = browser.find_element(
            By.CSS_SELECTOR, '.scroll-container'
        ).find_elements(By.CSS_SELECTOR, 'span')
        for el in element:
            if el.get_attribute('class') == 'last-of-list':
                flag = False
            if el not in data:
                el.find_element(By.CSS_SELECTOR, 'input').send_keys(Keys.DOWN)
                data.append(el)
                count.append(int(el.text))

print(sum(count))
