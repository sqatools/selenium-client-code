from .browser_actions import BrowserAction
from automation.data.test_data import *
from .locators import *
import pyautogui
from time import sleep
import tenacity as tenacity

class operation_loogbook(BrowserAction):
    def __init__(self, driver, wait_time):
        super().__init__(driver, wait_time)

    def click_to_operation(self):
        self.click_element(OPERATION_MENU_BUTTON)

    def click_to_logbook(self):
        self.click_element(LOGBOOK_MENU_OPTION)


    def navigate_to_logbook(self, check=None):
        """
        This method will navigate to logbook operation page
        :param check: this parameter is to check header of logbook page.
        :return:
        """
        try:
            if check is not None:
                if not self.verify_element_is_visible(LOGBOOK_HEADER):
                    self.click_to_operation()
                    self.click_to_logbook()
                    assert self.verify_element_is_visible(LOGBOOK_HEADER)
                else:
                    pass
            else:
                self.click_to_operation()
                self.click_to_logbook()
                assert self.verify_element_is_visible(LOGBOOK_HEADER)
        except Exception as e:
            self.take_screen_shot('logbook')
            raise (e)

    def click_add_logbook(self):
        self.click_element(ADD_LOGBOOK_ENTRY)

    def set_loogbook_event_time(self, event_date_time=None):
        if event_date_time is not None:
            self.input_text(CAL_INPUT_BOX, event_date_time)
        else:
            log_book_time = self.get_attribute_value(CAL_INPUT_BOX, "value")
            return log_book_time

    def select_event_status(self, status):
        self.click_element(STATUS_DROP_DOWN)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{status}']").click()

    def select_event_category1(self, category1):
        self.click_element(CATEGORY_DROP_DOWN1)
        self.input_text(CATEGORY_TEXT_BOX, category1)
        sleep(2)
        allelement = self.spdriver.find_elements_by_xpath("//div[@class='Select-menu-outer']//*")
        for elem in allelement:
            if elem.text == category1:
                elem.click()
                break
            else:
                continue

    def select_event_category2(self, category2):
        sleep(2)
        if self.verify_element_is_visible(CATEGORY_DROP_DOWN2):
            self.click_element(CATEGORY_DROP_DOWN2)
            self.input_text(CATEGORY_TEXT_BOX2, category2)
            sleep(2)
            allelement = self.spdriver.find_element_by_xpath("//div[@class='Select-menu-outer']//*")
            for elem in allelement:
                if elem.text == category2:
                    elem.click()
                    break
                else:
                    continue

    def select_event_priority(self, priority):
        self.click_element(PRIORITY_DROP_DOWN)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{priority}']").click()

    def select_event_area_site(self, site):
        self.click_element(LOG_BOOK_AREA_DROP_DOWN)
        self.spdriver.find_element_by_xpath(f"//*[text()='{site}']").click()

    def select_area_section(self, section):
        sleep(2)
        if self.verify_element_is_visible(LOG_BOOK_AREA_DROP_DOWN2):
            self.click_element(LOG_BOOK_AREA_DROP_DOWN2)
            self.spdriver.find_element_by_xpath(f"//*[text()='{section}']").click()
        else:
            pass

    def select_event_area_name(self, area):
        sleep(2)
        if self.verify_element_is_visible(LOG_BOOK_AREA_DROP_DOWN3):
            self.click_element(LOG_BOOK_AREA_DROP_DOWN3)
            self.spdriver.find_element_by_xpath(f"//*[text()='{area}']").click()
        else:
            pass

    def select_area_unit(self, unit):
        sleep(2)
        if self.verify_element_is_visible(LOG_BOOK_AREA_DROP_DOWN4):
            self.click_element(LOG_BOOK_AREA_DROP_DOWN4)
            self.spdriver.find_element_by_xpath(f"//*[text()='{unit}']").click()

    def select_logbook_equipment(self, asset_name):
        self.click_element(EQUIPMENT_BUTTON)
        self.input_text(ASSET_SEARCH_BOX, asset_name)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//span[contains(text(), '{asset_name}')]//parent::div").click()

    def click_on_confirm_button(self):
        self.click_element(CONFIRM_BUTTON)

    @tenacity.retry(
        wait=tenacity.wait_exponential(max=60),
        stop=tenacity.stop_after_attempt(10),
        retry=tenacity.retry_if_result(lambda result: result is False),
    )
    def open_logbook_event_popup(self):
        self.navigate_to_logbook()
        self.click_add_logbook()
        assert self.verify_element_is_visible(LOGBOOK_DETAIL_TAB)

    def enter_value_in_event_textbody(self, msg):
        self.switch_to_iframe(TEXT_AREA_IFRAME_ID)
        self.input_text(TEXT_FIELD_ID, msg)

    def attach_file(self, locator, filepath):
        self.click_element(locator)
        sleep(2)
        pyautogui.write(filepath)
        sleep(2)
        pyautogui.press('enter')

    def upload_file_in_logbook(self, link_url, link_desc, filepath):
        self.click_element(DROP_FILE_INITIATE_BUTTON)
        self.input_text(ATTACHMENT_LINK_TEXTBOX, link_url)
        self.input_text(LINK_DESCRIPTION_TEXT_BOX, link_desc)
        self.attach_file(DRAG_DROP_FILE_TO_UPLOAD, filepath)
        sleep(2)
        self.click_element(CONFIRM_BUTTON)

    def click_to_event_save_button(self):
        self.check_element_is_enabled(SAVE_BUTTON)
        self.click_element(SAVE_BUTTON)

    def click_to_logbook_breadcrumb(self):
        if self.verify_element_is_visible(LOOG_BOOK_BREDCRUM):
            self.click_element(LOOG_BOOK_BREDCRUM)

    def verify_new_logbook_time(self, logbooktime):
        rec_logbook_time = self.get_text_of_element(RECENTLY_ADDED_LOGBOOK_TIME)
        assert rec_logbook_time == logbooktime

    def verify_new_logbook_msg(self, msg):
        recent_msg = self.get_text_of_element(RECENTLY_ADDED_LOGBOOK_MSG)
        assert recent_msg == msg

    def add_log_book_event(self, kwargs):
        try:
            self.open_logbook_event_popup()
            self.switch_to_iframe(LOOG_BOOK_FRAME)
            event_time = None
            if "event_date" in kwargs:
                event_time = self.set_loogbook_event_time()
            if "status" in kwargs:
                self.select_event_status(kwargs['status'])
            if "category1" in kwargs:
                self.select_event_category1(kwargs['category1'])
            if "category2" in kwargs:
                self.select_event_category1(kwargs['category2'])
            if "priority" in kwargs:
                self.select_event_priority(kwargs['priority'])
            if "site" in kwargs:
                self.select_event_area_site(kwargs['site'])
            if "section" in kwargs:
                self.select_area_section(kwargs['section'])
            if "area" in kwargs:
                self.select_event_area_name(kwargs['area'])
            if "unit" in kwargs:
                self.select_area_unit(kwargs['unit'])
            if "asset_name" in kwargs:
                self.select_logbook_equipment(kwargs['asset_name'])
                self.click_on_confirm_button()
            if 'filepath' in kwargs:
                self.upload_file_in_logbook(kwargs['link_url'], kwargs['link_desc'], kwargs['filepath'])
            if 'event_msg' in kwargs:
                self.enter_value_in_event_textbody(kwargs['event_msg'])
            self.switch_to_default()
            self.switch_to_iframe(LOOG_BOOK_FRAME)
            sleep(3)
            self.click_to_event_save_button()
            sleep(2)
            self.switch_to_default()
            self.click_to_logbook_breadcrumb()
            #self.verify_new_logbook_time(event_time)
        except Exception as e:
            self.take_screen_shot("log_book")
            raise (e)


