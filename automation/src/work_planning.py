from .browser_actions import BrowserAction
from automation.data.test_data import *
from .locators import *
import pyautogui
from time import sleep
from pytest_html_reporter import attach

class workplanning(BrowserAction):
    def __init__(self, driver, wait_time):
        super().__init__(driver, wait_time)

    def click_to_operation(self):
        self.click_element(OPERATION_MENU_BUTTON)

    def click_to_work_planning(self):
        self.click_element(WP_MENU_OPTION)

    def navigate_work_planning(self, check=None):
        try:
            if check is not None:
                if not self.verify_element_is_visible(WP_HEADER):
                    self.click_to_operation()
                    self.click_to_work_planning()
                    sleep(5)
                    assert self.verify_element_is_visible(WP_HEADER)
                else:
                    pass
            else:
                self.click_to_operation()
                self.click_to_work_planning()
                sleep(5)
                assert self.verify_element_is_visible(WP_HEADER)
        except Exception as e:
            self.take_screen_shot('work_planning')
            raise (e)

    def wp_click_add_button(self):
        self.click_element(WP_ADD_BUTTON)

    def wp_plan_template_dropdown(self, plan):
        self.click_element(WP_PLAN_TEMPLATE_DROPDOWN)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{plan}']").click()
        sleep(2)

    def wp_site_dropdown(self, site):
        self.click_element(WP_SITE_DROPDOWN)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{site}']").click()
        sleep(2)

    def wp_section_dropdown(self, section):
        self.click_element(WP_SECTION_DROPDOWN)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{section}']").click()
        sleep(2)

    def wp_area_dropdown(self, area):
        sleep(2)
        if self.verify_element_is_visible(WP_AREA_DROPDOWN):
            self.click_element(WP_AREA_DROPDOWN)
            sleep(2)
            self.spdriver.find_element_by_xpath(f"//*[text()='{area}']").click()
            sleep(2)

    def wp_unit_dropdown(self, unit):
        sleep(2)
        if self.verify_element_is_visible(WP_UNIT_DROPDOWN):
            self.click_element(WP_UNIT_DROPDOWN)
            sleep(2)
            self.spdriver.find_element_by_xpath(f"//*[text()='{unit}']").click()
            sleep(2)

    def wp_category_dropdown(self, category):
        sleep(2)
        if self.verify_element_is_visible(WP_WORK_CATEGORY_DROPDOWN):
            self.click_element(WP_WORK_CATEGORY_DROPDOWN)
            sleep(2)
            self.spdriver.find_element_by_xpath(f"//*[text()='{category}']").click()
            sleep(2)

    def wp_assigned_group(self, groupname):
        self.click_element(WP_ASSIGNED_GROUP_DROPDOWN)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{groupname}']").click()
        sleep(2)

    def wp_industraform(self, instraform):
        self.click_element(WP_INDUSTRFORM_DROPDOWN)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{instraform}']").click()
        sleep(2)

    def wp_schedule_type(self, schedule):
        self.click_element(WP_SCHEDULE_TYPE)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{schedule}']").click()
        sleep(2)

    def wp_start_date(self, date):
        self.input_text(WP_START_DATE, date)
        sleep(2)

    def wp_start_time(self, time):
        self.input_text(WP_START_TIME, time)
        sleep(2)

    def wp_finish_date(self, date):
        self.input_text(WP_FINISH_DATE, date)
        sleep(2)

    def wp_finish_time(self, time):
        self.input_text(WP_FINISH_TIME, time)
        sleep(2)

    def wp_time_zone(self, timezone=None):
        if timezone is not None:
            self.click_element(WP_TIMEZONE)
            self.input_text(WP_TIMEZONE_TEXTFIELD, timezone)
            sleep(2)
            self.spdriver.find_element_by_xpath(f"//*[text()='{timezone}']").click()
        else:
            pass

    def wp_upload_attachment(self, filepath):
        self.click_element(WP_ADD_ATTACHMENT)
        sleep(5)
        self.switch_to_iframe(SO_UPLOAD_IFRAME)
        self.spdriver.find_element_by_name('filedata').send_keys(filepath)
        sleep(5)
        self.switch_to_default()

    def wp_message_box(self, message):
        self.switch_to_iframe(WP_MESSAGE_IFRAME)
        sleep(2)
        self.input_text(MESSAGE_BOX_ID, message)
        sleep(2)
        self.switch_to_default()

    def wp_click_to_breadcrumb(self):
        if self.verify_element_is_visible(WI_BREAD_CRUMB):
            self.click_element(WI_BREAD_CRUMB)

    def wp_verify_message(self, msg):
        wi_msg = self.get_text_of_element(WP_DESCRIPTION_MSG)
        assert wi_msg == msg

    def create_work_planning(self, kwargs):
        try :
            self.navigate_work_planning()
            self.wp_click_add_button()
            sleep(20)
            if 'plan' in kwargs:
                self.wp_plan_template_dropdown(kwargs['plan'])
            if 'site' in kwargs:
                self.wp_site_dropdown(kwargs['site'])
            if 'section' in kwargs:
                self.wp_section_dropdown(kwargs['section'])
            if 'area' in kwargs:
                self.wp_area_dropdown(kwargs['area'])
            if 'unit' in kwargs:
                self.wp_unit_dropdown(kwargs['unit'])
            if 'category' in kwargs:
                self.wp_category_dropdown(kwargs['category'])
            if 'industra' in kwargs:
                self.wp_industraform(kwargs['industra'])
            if 'schedule' in kwargs:
                self.wp_schedule_type(kwargs['schedule'])
            if 'start_date' in kwargs:
                self.wp_start_date(kwargs['start_date'])
            if 'start_time' in kwargs:
                self.wp_start_time(kwargs['start_time'])
            if 'finish_date' in kwargs:
                self.wp_finish_date(kwargs['finish_date'])
            if 'finish_time' in kwargs:
                self.wp_finish_time(kwargs['finish_time'])
            if 'timezone' in kwargs:
                self.wp_time_zone(kwargs['timezone'])
            if 'filepath' in kwargs:
                self.wp_upload_attachment(kwargs['filepath'])
            self.wp_message_box(kwargs['message'])
            sleep(5)
            self.click_element(WP_SAVE_BUTTON)
            sleep(5)
            self.wp_click_to_breadcrumb()
            sleep(5)
            self.wp_verify_message(kwargs['message'])
        except Exception as e:
            attach(data=self.spdriver.get_screenshot_as_png())
            raise(e)