from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.10/2/index.html')
    green_squares = [
        browser.find_element(By.CSS_SELECTOR, f'#draganddrop{i}')
        for i in range(1, 11)
    ]
    gray_zone = browser.find_element(By.CSS_SELECTOR, '.draganddrop_end')
    actions = ActionChains(browser)

    for square in green_squares:
        actions.drag_and_drop(square, gray_zone).perform()

    result = browser.find_element(By.CSS_SELECTOR, '#message').text
    print(result)
