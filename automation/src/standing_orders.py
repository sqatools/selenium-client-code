from .browser_actions import BrowserAction
from automation.data.test_data import *
from .locators import *
import pyautogui
from time import sleep
import tenacity as tenacity

class standing_orders(BrowserAction):
    def __init__(self, driver, wait_time):
        super().__init__(driver, wait_time)

    def click_to_operation(self):
        self.click_element(OPERATION_MENU_BUTTON)

    def click_to_standing_orders(self):
        self.click_element(SO_MENU_OPTION)

    def navigate_standing_orders(self, check=None):
        try:
            if check is not None:
                if not self.verify_element_is_visible(SO_HEADER):
                    self.click_to_operation()
                    self.click_to_standing_orders()
                    sleep(5)
                    assert self.verify_element_is_visible(SO_HEADER)
                else:
                    pass
            else:
                self.click_to_operation()
                self.click_to_standing_orders()
                sleep(5)
                assert self.verify_element_is_visible(SO_HEADER)
        except Exception as e:
            self.take_screen_shot('standing_order')
            raise (e)

    def so_select_site(self, site):
        sleep(2)
        self.click_element(SO_SITE_DROPDOWN)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{site}']").click()
        sleep(2)

    def so_select_section(self, section):
        self.click_element(SO_SECTION_DROPDOWN)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{section}']").click()
        sleep(5)

    def so_select_area(self, area):
        self.click_element(SO_AREA_DROPDOWN)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{area}']").click()
        sleep(2)

    def so_select_unit(self, unit):
        self.click_element(SO_UNIT_DROPDOWN)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{unit}']").click()
        sleep(2)

    def so_start_date(self, date):
        self.input_text(SO_START_DATE, date)

    def so_start_time(self, time):
        self.input_text(SO_START_TIME, time)

    def so_end_date(self, date):
        self.input_text(SO_END_DATE, date)

    def so_end_time(self, time):
        self.input_text(SO_END_TIME, time)

    def so_renewal_period(self, period, schedule=None):
        self.input_text(SO_RENEWAL_PERIOD, period)
        if schedule is not None:
            self.click_element(SO_RENEWAL_SCHEDULE)
            sleep(2)
            self.spdriver.find_element_by_xpath(f"//*[text()='{schedule}']").click()
            sleep(2)
        else:
            pass

    def so_upload_attachment(self, filepath):
        self.click_element(SO_ATTACHMENT_BUTTON)
        sleep(5)
        self.switch_to_iframe(SO_UPLOAD_IFRAME)
        #self.input_text(SO_BROWSE_BUTTON, filepath)
        self.spdriver.find_element_by_name('filedata').send_keys(filepath)
        sleep(5)
        self.switch_to_default()

    def so_email_target_group(self, check=None):
        if check is None:
            self.click_element(SO_EMAIL_TARGET_CHECKBOX)
        else:
            pass

    def so_select_all_taget_group(self):
        self.click_element(SO_SELECT_ALL_TARGET_GROUP)

    def so_select_none_target_group(self):
        self.click_element(SO_SELECT_NONE_TARGET_GROUP)

    def so_invert_selection_target_group(self):
        self.click_element(SO_SELECT_INVERT_TARGET_GROUP)

    def so_select_speficic_target_group(self, group_name):
        element = f"//div[text()='{group_name}']//parent::div//input[contains(@id,'dijit_form_CheckBox')]"
        self.click_element((XPATH, element))

    def so_select_status(self, status):
        self.click_element(SO_SELECT_STATUS)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{status}']").click()
        sleep(5)

    def so_save_button(self):
        self.click_element(SO_SAVE_BUTTON)

    def so_click_add_button(self):
        self.click_element(ADD_BUTTON)

    def so_orders(self):
        orders = self.get_text_of_element(SO_ORDER)
        return orders

    def create_standing_order(self, kwargs):
        self.navigate_standing_orders()
        self.so_click_add_button()
        if "site" in kwargs:
            self.so_select_site(kwargs['site'])
        if "section" in kwargs:
            self.so_select_section(kwargs['section'])
        if "area" in kwargs:
            self.so_select_area(kwargs['area'])
        if "unit" in kwargs:
            self.so_select_unit(kwargs['unit'])
        if "start_date" in kwargs:
            self.so_start_date(kwargs['start_date'])
        if "start_time" in kwargs:
            self.so_start_time(kwargs['start_time'])
        if "end_date" in kwargs:
            self.so_end_date(kwargs['end_date'])
        if "end_time" in kwargs:
            self.so_end_date(kwargs['end_time'])
        if "renewal_period" in kwargs:
            self.so_renewal_period(kwargs['renewal_period'], kwargs['renewal_schedule'])
        if "file_path" in kwargs:
            self.so_upload_attachment(kwargs['file_path'])
        if "email_target" in kwargs:
            self.so_email_target_group(kwargs['email_target'])
        if "target_group" in kwargs:
            if kwargs['target_group'] == "select_all":
                self.so_select_all_taget_group()
            elif kwargs['target_group'] == "select_none":
                self.so_select_none_target_group()
            elif kwargs['target_group']  == "invert_selection":
                self.so_invert_selection_target_group()
            else:
                self.so_select_speficic_target_group(kwargs['target_group'])
        if "status" in kwargs:
            self.so_select_status(kwargs['status'])
        self.switch_to_iframe(SO_IFRAME_XPATH)
        self.input_text(SO_BODY_TEXT, kwargs['so_msg'])
        sleep(2)
        self.switch_to_default()
        self.so_save_button()
        sleep(5)
        self.click_element(SO_BREAD_CRUMB)
        sleep(2)
        assert self.so_orders() == kwargs['so_msg']