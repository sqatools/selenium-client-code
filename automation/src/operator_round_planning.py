from .browser_actions import BrowserAction
from automation.data.test_data import *
from .locators import *
import pyautogui
from time import sleep
import tenacity as tenacity

class operator_round_planning(BrowserAction):
    def __init__(self, driver, wait_time):
        super().__init__(driver, wait_time)

    def click_to_operation(self):
        self.click_element(OPERATION_MENU_BUTTON)

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
        self.spdriver.find_element_by_name(ORP_CHOOSE_UPLOAD_FILE[1]).send_keys(sheet_path)
        sleep(5)
        if confirm is not None:
            self.click_element(ORP_CONFIRM_UPLOAD_BUTTON)
        else:
            self.click_element(ORP_CANCEL_BUTTON)
        sleep(2)

    def orp_upload_static_file(self, static_filepath, confirm="yes"):
        self.click_element(ORP_UPLOAD_STATIC_FILE)
        sleep(2)
        self.spdriver.find_element_by_name(ORP_CHOOSE_UPLOAD_FILE[1]).send_keys(static_filepath)
        sleep(5)
        if confirm is not None:
            self.click_element(ORP_CONFIRM_UPLOAD_BUTTON)
        else:
            self.click_element(ORP_CANCEL_BUTTON)
        sleep(2)

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