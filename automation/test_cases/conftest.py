import pytest
from selenium import webdriver
from automation.src.common_feature import common
from automation.data.test_data import *

def get_driver(browser):
        if browser == 'chrome':
            chrome_options = webdriver.ChromeOptions()
            if headless == "true":
                chrome_options.add_argument("headless")
            driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
            driver.maximize_window()
            driver.implicitly_wait(20)
            return driver
        elif browser == 'firefox':
            driver = webdriver.Firefox(executable_path=firefox_driver_path)
            driver.maximize_window()
            driver.implicitly_wait(20)
            return driver
        elif browser == 'edge':
            driver = webdriver.Edge(executable_path=edge_driver_path)
            driver.maximize_window()
            driver.implicitly_wait(20)
            return driver

@pytest.fixture(scope='session')
def setup():
    driver = get_driver(browser)
    obj = common(driver, wait_time)
    obj.login()
    return obj