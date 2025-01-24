import time

from selenium.webdriver.common.by import By

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.7/1/index.html')
    time.sleep(2)

    uranium_pieces = browser.find_elements(By.CSS_SELECTOR, '.clickMe')

    for piece in uranium_pieces:
        browser.execute_script(
            'return arguments[0].scrollIntoView(true);', piece
        )
        piece.click()

    time.sleep(1)
    alert = browser.switch_to.alert
    result = alert.text
    print(result)
    alert.accept()
