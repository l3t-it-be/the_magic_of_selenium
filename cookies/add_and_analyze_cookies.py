import ast
import time

from selenium.webdriver.common.by import By

from browser_setup import browser

with open('cookies.txt', encoding='utf-8') as cookie_file:
    cookies = ast.literal_eval(cookie_file.read().split('=', 1)[1].strip())

with browser:
    min_age = float('inf')
    max_number_of_skills = -float('inf')
    the_very_cookie = None

    for cookie in cookies:
        browser.get('https://parsinger.ru/selenium/5.6/1/index.html')
        browser.delete_all_cookies()
        browser.refresh()
        browser.add_cookie(cookie)
        browser.refresh()
        time.sleep(2)

        age = int(
            browser.find_element(By.CSS_SELECTOR, '#age')
            .text.strip()
            .split()[-1]
        )
        number_of_skills = len(
            browser.find_elements(By.CSS_SELECTOR, '#skillsList li')
        )

        if age < min_age and number_of_skills > max_number_of_skills:
            min_age = age
            max_number_of_skills = number_of_skills
            the_very_cookie = cookie

    if the_very_cookie:
        browser.get('https://parsinger.ru/selenium/5.6/1/index.html')
        browser.delete_all_cookies()
        browser.refresh()
        browser.add_cookie(the_very_cookie)
        browser.refresh()
        cookies = browser.get_cookies()
        for cookie in cookies:
            if cookie['name'] == the_very_cookie['name']:
                print(
                    f'Developer to hire:\nAge: {min_age}, Number of Skills: {max_number_of_skills}'
                    f'\nCookie: \nname: {cookie['name']} value: {cookie['value']}'
                )
                break
    else:
        print('No valid cookie found.')
