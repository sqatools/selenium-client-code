import pyautogui
from time import sleep
import tenacity as tenacity
from .browser_actions import *
from .operation_logbook import operation_loogbook
from .operator_round_planning import operator_round_planning
from .standing_orders import standing_orders
from .work_instructions import work_instructions
from .work_planning import workplanning
from .event_manager import event_manager
from automation.data.test_data import *
from .locators import *
from automation.data.test_variables import *


class common(BrowserAction):
    def __init__(self, driver, wait_time):
        super().__init__(driver, wait_time)
        self.olb = operation_loogbook(driver, wait_time)
        self.orp = operator_round_planning(driver, wait_time)
        self.so = standing_orders(driver, wait_time)
        self.wi = work_instructions(driver, wait_time)
        self.wp = workplanning(driver, wait_time)
        self.em = event_manager(driver, wait_time)

    def search_data_on_google(self, search_input=None):
        self.launch_url(product_url)
        if search_input is None:
            self.input_text(GOOGLE_SEARCH_BOX, search_value)
        else:
            self.input_text(GOOGLE_SEARCH_BOX, search_input)
        self.click_element(GOOGLE_SEARCH_BUTTON)
        self.take_screen_shot('search')

    def login(self, username=Username, password=Password):
        self.launch_url(product_url)
        self.input_text(LOGIN_USERNAME, username)
        self.input_text(LOGIN_PASSWORD, password)
        self.click_element(LOGIN_TERMS_CHECKBOX)
        self.click_element(LOGIN_BUTTON)
        self.take_screen_shot('login')
        assert self.verify_element_is_visible(APPLICATION_HOME_PAGE_NAV)