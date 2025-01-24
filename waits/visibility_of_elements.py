import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser_setup import browser

ids_to_find = [
    'xhkVEkgm',
    'QCg2vOX7',
    '8KvuO5ja',
    'CFoCZ3Ze',
    '8CiPCnNB',
    'XuEMunrz',
    'vmlzQ3gH',
    'axhUiw2I',
    'jolHZqD1',
    'ZM6Ms3tw',
    '25a2X14r',
    'aOSMX9tb',
    'YySk7Ze3',
    'QQK13iyY',
    'j7kD7uIR',
]

with browser:
    browser.get('https://parsinger.ru/selenium/5.9/3/index.html')

    ids_to_click = []
    for id_to_find in ids_to_find:
        element = WebDriverWait(browser, 30).until(
            ec.visibility_of_element_located((By.ID, id_to_find))
        )
        ids_to_click.append(element)

    time.sleep(0.5)

    for id_el in ids_to_click:
        id_el.click()
        time.sleep(0.5)

    alert = browser.switch_to.alert
    result = alert.text
    print(result)
    alert.accept()
