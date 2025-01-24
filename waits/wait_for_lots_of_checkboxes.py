from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.9/7/index.html')

    checkboxes = browser.find_elements(
        By.CSS_SELECTOR, 'input[type="checkbox"]'
    )
    buttons = browser.find_elements(By.CSS_SELECTOR, 'button')

    for checkbox, button in zip(checkboxes, buttons):
        WebDriverWait(browser, 5).until(ec.element_to_be_selected(checkbox))
        button.click()

    result = browser.find_element(By.CSS_SELECTOR, '#result').text
    print(result)
