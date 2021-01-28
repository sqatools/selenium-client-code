from .browser_actions import BrowserAction
from automation.data.test_data import *
from .locators import *
import pyautogui
from time import sleep
import tenacity as tenacity

class operation(BrowserAction):
    def __init__(self, driver, wait_time):
        super().__init__(driver, wait_time)

    def click_to_operation(self):
        self.click_element(OPERATION_MENU_BUTTON)

    def click_to_logbook(self):
        self.click_element(LOGBOOK_MENU_OPTION)

    def navigate_to_logbook(self):
        try:
            if not self.verify_element_is_visible(LOGBOOK_HEADER):
                self.click_to_operation()
                self.click_to_logbook()
                assert self.verify_element_is_visible(LOGBOOK_HEADER)
            else:
                pass
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


    def click_operator_round_planning(self):
        self.click_element(ORP_MENU_OPTION)

    def navigate_to_orp(self, check=None):
        try:
            if check is not None:
                if not self.verify_element_is_visible(ORP_HEADER):
                    self.click_to_operation()
                    self.click_operator_round_planning()
                    assert self.verify_element_is_visible(ORP_HEADER)
                else:
                    pass
            else:
                self.click_to_operation()
                self.click_operator_round_planning()
                assert self.verify_element_is_visible(ORP_HEADER)
        except Exception as e:
            self.take_screen_shot('orp')
            raise (e)

    def click_add_button(self):
        self.click_element(ADD_BUTTON)

    def orp_enter_title(self, title):
        self.input_text(ORP_TITLE, title)

    def orp_select_site(self, site):
        sleep(5)
        self.click_element(ORP_SITE_DROPDOWN)
        self.spdriver.find_element_by_xpath(f"//*[text()='{site}']").click()

    def orp_select_section(self, section):
        sleep(2)
        self.click_element(ORP_SECTION_DROPDOWN)
        sleep(2)
        element = self.spdriver.find_element_by_xpath(f"//*[contains(text(),'{section}')]")
        element.click()

    def orp_select_area(self, area):
        sleep(2)
        self.click_element(ORP_AREA_DROPDOWN)
        element = self.spdriver.find_element_by_xpath(f"//*[text()='{area}']")
        sleep(2)
        element.click()

    def orp_select_unit(self, unit):
        sleep(5)
        self.click_element(ORP_UNIT_DROPDOWN)
        element = self.spdriver.find_element_by_xpath(f"//*[contains(text(),'{unit}')]")
        sleep(2)
        element.click()

    def orp_select_round_type(self, round_type):
        sleep(5)
        self.click_element(ORP_ROUND_TYPE_DROPDOWN)
        element = self.spdriver.find_element_by_xpath(f"//*[text()='{round_type}']")
        sleep(2)
        element.click()

    def orp_select_assigned_group(self, assigned_group):
        sleep(2)
        self.click_element(ORP_ASSIGNED_GROUP_DROPDOWN)
        sleep(2)
        element = self.spdriver.find_element_by_xpath(f"//*[text()='{assigned_group}']")
        element.click()

    def orp_select_schedule_type(self, schedule):
        sleep(2)
        self.click_element(ORP_SCHEDULED_TYPE_DROPDOWN)
        element = self.spdriver.find_element_by_xpath(f"//*[text()='{schedule}']")
        sleep(2)
        element.click()

    def orp_start_date(self, start_date=None, start_time=None):
        if start_date is not None:
            self.input_text(ORP_START_DATE, start_date)
        else:
            pass
        if start_date is not None:
            self.input_text(ORP_START_TIME, start_time)
        else:
            pass

    def orp_finish_date(self, finish_date=None, finish_time=None):
        if finish_date is not None:
            self.input_text(ORP_FINISH_DATE, finish_date)
        else:
            pass
        if finish_time is not None:
            self.input_text(ORP_FINISH_TIME, finish_time)
        else:
            pass

    def orp_select_time_zone(self, timezone):
        if timezone is not None:
            self.click_element(ORP_TIMEZONE_DROPDOWN)
            self.input_text(ORP_TIMEZONE_TEXTFIELD, timezone)
        else:
            pass

    def orp_set_repeat(self, repeat_times=None, repeat_schedule=None):
        if repeat_times is not None:
            self.input_text(ORP_REPEAT_EVERY_TEXT_FIELD, repeat_times)
        else:
            pass
        if repeat_schedule is not None:
            self.click_element(ORP_REPEAT_EVERY_DROP_DOWN)
            sleep(2)
            self.spdriver.find_element_by_xpath(f"//*[text()='{repeat_schedule}']").click()
        else:
            pass

    def orp_additional_dates(self, dates):
        self.input_text(ORP_ADDITIONAL_DATES, dates)

    def orp_excluded_dates(self, dates):
        self.input_text(ORP_EXCLUDED_DATES, dates)

    def orp_duration(self, duration=None):
        if duration is not  None:
            self.input_text(ORP_DURATION, duration)
        else:
            pass

    def orp_click_breakcrumb(self):
        self.click_element(ORP_BREAD_CRUMP)

    def orp_get_title_header(self):
        title = self.get_text_of_element(OPR_TITLE_HEADER)
        return title

    def orp_upload_task_spreadsheet(self, sheet_path, confirm='yes'):
        self.click_element(ORP_UPLOAD_TASK_SPREADSHEET)
        sleep(2)
        self.click_element(ORP_CHOOSE_UPLOAD_FILE)
        sleep(2)
        pyautogui.write(sheet_path)
        sleep(2)
        pyautogui.press('enter')
        if confirm is not None:
            self.click_element(ORP_CONFIRM_UPLOAD_BUTTON)
        else:
            self.click_element(ORP_CANCEL_BUTTON)

    def orp_upload_static_file(self, static_filepath, confirm="yes"):
        self.click_element(ORP_UPLOAD_STATIC_FILE)
        self.click_element(ORP_CHOOSE_UPLOAD_FILE)
        sleep(2)
        pyautogui.write(static_filepath)
        sleep(2)
        pyautogui.press('enter')
        if confirm is not None:
            self.click_element(ORP_CONFIRM_UPLOAD_BUTTON)
        else:
            self.click_element(ORP_CANCEL_BUTTON)

    def orp_download_task_spreadsheet(self, filename):
        self.click_element(ORP_DOWNLOAD_TASKS_SPREADSHEET)
        sleep(20)
        filepath = os.path.join(download_path, filename)
        assert os.path.isfile(filepath)

    def create_operator_round_planning(self, kwargs):
        self.navigate_to_orp()
        self.click_add_button()
        if "title" in kwargs:
            self.orp_enter_title(kwargs['title'])
        if "site" in kwargs:
            self.orp_select_site(kwargs['site'])
        if "section" in kwargs:
            self.orp_select_section(kwargs['section'])
        if "area" in kwargs:
            self.orp_select_area(kwargs['area'])
        if "unit" in kwargs:
            self.orp_select_unit(kwargs['unit'])
        if "round_type" in kwargs:
            self.orp_select_round_type(kwargs['round_type'])
        if "assigned_group" in kwargs:
            self.orp_select_assigned_group(kwargs['assigned_group'])
        if "schedule_type" in kwargs:
            self.orp_select_schedule_type(kwargs['schedule_type'])
        if "start_date" in kwargs:
            self.orp_start_date(start_date=kwargs['start_date'])
        if "start_time" in kwargs:
            self.orp_start_date(start_time=kwargs['start_time'])
        if "finish_date" in kwargs:
            self.orp_finish_date(finish_date=kwargs['finish_date'])
        if "finish_time" in kwargs:
            self.orp_finish_date(finish_time=kwargs['finish_time'])
        if "timezone" in kwargs:
            self.orp_select_time_zone(kwargs['timezone'])
        if "repeat_times" in kwargs:
            self.orp_set_repeat(repeat_times=kwargs['repeat_times'])
        if "repeat_schedule" in kwargs:
            self.orp_set_repeat(repeat_schedule=kwargs['repeat_schedule'])
        if "additional_dates" in kwargs:
            self.orp_additional_dates(kwargs['additional_dates'])
        if "excluded_dates" in kwargs:
            self.orp_excluded_dates(kwargs['excluded_dates'])
        if "duration" in kwargs:
            self.orp_duration(kwargs['duration'])
        if "description_text" in kwargs:
            self.switch_to_iframe(ORP_TEXT_FIELD_IFRAME)
            sleep(2)
            self.input_text(ORP_BODY_TEXT, kwargs['description_text'])
            sleep(2)
            self.switch_to_default()
        self.click_element(ORP_SAVE_BUTTON)
        sleep(10)
        if "sheet_path" in kwargs:
            self.orp_upload_task_spreadsheet(kwargs['sheet_path'], kwargs["sheet_upload_confirm"])
            sleep(10)
        if "static_path" in kwargs:
            self.orp_upload_static_file(kwargs['static_path'], kwargs["sheet_upload_confirm"])
            sleep(10)
        if "download_sheet" in kwargs:
            self.orp_download_task_spreadsheet(f"{kwargs['title']}.form.xlsx")
            sleep(10)
        self.orp_click_breakcrumb()
        sleep(5)
        assert kwargs['title']  == self.orp_get_title_header()

### Standing Orders ####

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
        sleep(2)
        #self.click_element(SO_BROWSE_BUTTON)
        self.input_text(SO_BROWSE_BUTTON, filepath)
        sleep(2)
        #pyautogui.write(filepath)
        #sleep(2)
        #pyautogui.press('enter')

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

    def create_standing_order(self, kwargs):
        self.navigate_standing_orders()
        self.click_add_button()
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

