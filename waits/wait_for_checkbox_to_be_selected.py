from selenium.webdriver.common.by import By

from browser_setup import browser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

with browser:
    browser.get('https://parsinger.ru/selenium/5.9/6/index.html')

    checkbox = browser.find_element(By.CSS_SELECTOR, 'input#myCheckbox')
    WebDriverWait(browser, 5).until(ec.element_to_be_selected(checkbox))
    browser.find_element(By.CSS_SELECTOR, 'button').click()

    result = browser.find_element(By.CSS_SELECTOR, '#result').text
    print(result)
