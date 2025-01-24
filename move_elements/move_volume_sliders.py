from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.10/6/index.html')

    sliders = browser.find_elements(By.CSS_SELECTOR, '.volume-slider')
    target_values = browser.find_elements(By.CSS_SELECTOR, '.target-value')

    for slider, target_value in zip(sliders, target_values):
        target_value = int(target_value.text)
        current_value = int(slider.get_attribute('value'))

        while current_value != target_value:
            if current_value < target_value:
                slider.send_keys(Keys.ARROW_RIGHT)
                current_value += 1
            elif current_value > target_value:
                slider.send_keys(Keys.ARROW_LEFT)
                current_value -= 1

    result = browser.find_element(By.CSS_SELECTOR, '#message').text
    print(result)
