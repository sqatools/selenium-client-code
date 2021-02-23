from .browser_actions import BrowserAction
from .locators import *
from time import sleep

class filter(BrowserAction):
    def __init__(self, driver):
        super().__init__(driver)

    def category_filter(self, category):
        self.click_element(FILTER_CATEGORY_DROPDOWN)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{category}']").click()

    def status_filter(self, status):
        self.click_element(FILTER_STATUS_DROPDOWN)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{status}']").click()

    def priority_filter(self, priority):
        self.click_element(FILTER_PRIORITY_DROPDOWN)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{priority}']").click()

    def site_filter(self, site):
        self.click_element(FILTER_SITE_DROPDOWN)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{site}']").click()
