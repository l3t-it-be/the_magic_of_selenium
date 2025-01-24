from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.9/4/index.html')
    browser.find_element(By.CSS_SELECTOR, 'span.close').click()

    WebDriverWait(browser, 5).until(
        ec.invisibility_of_element_located((By.CSS_SELECTOR, '#ad'))
    )
    browser.find_element(By.CSS_SELECTOR, 'button').click()
    message = browser.find_element(By.CSS_SELECTOR, '#message').text
    print(message)
