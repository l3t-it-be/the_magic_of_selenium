from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.5/5/1.html')
    containers = browser.find_elements(By.CSS_SELECTOR, '#main-container>div')

    for container in containers:
        color_code = container.find_element(By.CSS_SELECTOR, 'span').text

        dropdown = Select(container.find_element(By.CSS_SELECTOR, 'select'))
        dropdown.select_by_visible_text(color_code)

        container.find_element(
            By.CSS_SELECTOR, f'button[data-hex="{color_code}"]'
        ).click()

        container.find_element(
            By.CSS_SELECTOR, 'input[type="checkbox"]'
        ).click()
        container.find_element(
            By.CSS_SELECTOR, 'input[type="text"]'
        ).send_keys(color_code)

        container.find_element(
            By.XPATH, '//button[text()="Проверить"]'
        ).click()

    browser.find_element(
        By.XPATH, '//button[text()="Проверить все элементы"]'
    ).click()

    alert = browser.switch_to.alert
    result = alert.text
    print(result)
    alert.accept()
