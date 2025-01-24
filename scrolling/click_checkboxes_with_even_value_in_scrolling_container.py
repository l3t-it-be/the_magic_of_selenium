import time
from selenium.webdriver.common.by import By
from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.7/4/index.html')

    container = browser.find_element(By.CSS_SELECTOR, '#main_container')
    last_height = browser.execute_script(
        'return arguments[0].scrollHeight', container
    )

    while True:
        browser.execute_script(
            'arguments[0].scrollTop = arguments[0].scrollHeight', container
        )
        time.sleep(1)

        new_height = browser.execute_script(
            'return arguments[0].scrollHeight', container
        )
        if new_height == last_height:
            break
        last_height = new_height

    containers = browser.find_elements(By.CSS_SELECTOR, '.child_container')
    for container in containers:
        checkboxes = container.find_elements(
            By.CSS_SELECTOR, 'input[type="checkbox"]'
        )
        for checkbox in checkboxes:
            value = int(checkbox.get_attribute('value'))
            if value % 2 == 0:
                checkbox.click()

    button = browser.find_element(By.CSS_SELECTOR, '.alert_button')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    time.sleep(0.5)
    button.click()
    time.sleep(0.5)

    alert = browser.switch_to.alert
    result = alert.text
    print(result)
    alert.accept()
