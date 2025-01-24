import time

from selenium.webdriver.common.by import By

from browser_setup import browser

titles_sum = 0
with browser:
    browser.get('https://parsinger.ru/blank/3/index.html')
    buttons = browser.find_elements(By.CSS_SELECTOR, 'input[type="button"]')
    time.sleep(1)

    for button in buttons:
        button.click()

        tabs = browser.window_handles
        browser.switch_to.window(tabs[-1])
        title = int(browser.title)
        titles_sum += title
        browser.switch_to.window(tabs[0])

    print(titles_sum)
