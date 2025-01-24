from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from browser_setup import browser

full_code = []
with browser:
    browser.get('https://parsinger.ru/selenium/5.9/5/index.html')

    elements = browser.find_elements(By.CSS_SELECTOR, '#main_container div')
    for element in elements:
        element.click()
        browser.find_element(By.CSS_SELECTOR, '#close_ad').click()

        WebDriverWait(browser, 10).until(lambda _: element.text.strip() != '')
        code = element.text.strip()
        full_code.append(code)

print('-'.join(full_code))
