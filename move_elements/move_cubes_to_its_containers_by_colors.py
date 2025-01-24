from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.10/8/index.html')
    cubes = [
        browser.find_element(By.CSS_SELECTOR, f'#piece_{i}')
        for i in range(100, 801, 100)
    ]
    containers = [
        browser.find_element(By.CSS_SELECTOR, f'#range_{i}')
        for i in range(100, 801, 100)
    ]

    actions = ActionChains(browser)
    for cube, container in zip(cubes, containers):
        actions.drag_and_drop(cube, container).perform()

    result = browser.find_element(By.CSS_SELECTOR, '#message').text
    print(result)
