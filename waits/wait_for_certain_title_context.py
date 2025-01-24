from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/expectations/4/index.html')

    button = browser.find_element(By.CSS_SELECTOR, '#btn')
    WebDriverWait(browser, 5).until(ec.element_to_be_clickable(button))
    button.click()

    if WebDriverWait(browser, 20).until(ec.title_contains('JK8HQ')):
        result = browser.title
    print(result)
