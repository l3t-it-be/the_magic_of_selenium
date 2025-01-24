from selenium.webdriver.common.by import By

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/4/4.html')

    for checkbox in browser.find_elements(By.CSS_SELECTOR, 'input.check'):
        checkbox.click()
    browser.find_element(By.CSS_SELECTOR, 'input.btn').click()

    result = browser.find_element(By.CSS_SELECTOR, '#result').text
    print(result)
