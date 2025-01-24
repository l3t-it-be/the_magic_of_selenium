from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def create_driver():
    service = Service(executable_path=ChromeDriverManager().install())

    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    driver_options.add_argument('--start-maximized')
    driver_options.add_argument('--disable-notifications')
    driver_options.add_argument(f'user-agent={UserAgent().random}')

    driver = webdriver.Chrome(service=service, options=driver_options)
    driver.implicitly_wait(5)
    return driver


browser = create_driver()
