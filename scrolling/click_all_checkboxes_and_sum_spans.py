from selenium.webdriver.common.by import By

from browser_setup import browser

numbers = []
with browser:
    browser.get('https://parsinger.ru/scroll/2/index.html')
    checkboxes = browser.find_elements(
        By.CSS_SELECTOR, 'input[type="checkbox"]'
    )
    spans = browser.find_elements(By.CSS_SELECTOR, 'span')
    for checkbox in checkboxes:
        checkbox.click()
    for span in spans:
        if span.text.isdigit():
            numbers.append(int(span.text))

print(sum(numbers))
