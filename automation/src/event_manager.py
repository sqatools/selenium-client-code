from .browser_actions import BrowserAction
from automation.data.test_data import *
from .locators import *
import pyautogui
from time import sleep
from pytest_html_reporter import attach

class event_manager(BrowserAction):
    def __init__(self, driver, wait_time):
        super().__init__(driver, wait_time)

    def click_to_event_manager(self):
        self.click_element(EVENT_MANAGER_MENU_OPTION)

    def click_to_tag_watch_list(self):
        self.click_element(TAG_WATCH_LIST_MENU_OPTION)

    def navigate_to_tag_watch_list(self, check=None):
        try:
            if check is not None:
                if not self.verify_element_is_visible(TWL_HEADER):
                    self.click_to_event_manager()
                    self.click_to_tag_watch_list()
                    sleep(5)
                    assert self.verify_element_is_visible(TWL_HEADER)
                else:
                    pass
            else:
                self.click_to_event_manager()
                self.click_to_tag_watch_list()
                sleep(5)
                assert self.verify_element_is_visible(TWL_HEADER)
        except Exception as e:
            self.take_screen_shot('tag_watch_list')
            raise (e)

    def twl_click_add_button(self):
        self.click_element(WP_ADD_BUTTON)

    def twl_tag_textfield(self, tag):
        self.input_text(TWL_TAG, tag)

    def twl_variable_type_dropdown(self, variable):
        self.click_element(TWL_VARIABLE_TYPE_DROPDOWN)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{variable}']").click()
        sleep(2)

    def twl_data_type_dropdown(self, data_type):
        self.click_element(TWL_DATA_TYPE_DROPDOWN)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{data_type}']").click()
        sleep(2)


    def twl_datasource_dropdown(self, datasource):
        self.click_element(TWL_DATASOURCE_DROPDOWN)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{datasource}']").click()
        sleep(2)

    def twl_datasource_tag_dropdown(self, datasource_tag):
        self.click_element(TWL_DATASOURCE_TAG_DROPDOWN)
        sleep(2)
        self.input_text(TWL_DATASOURCE_TAG_TEXT, datasource_tag)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{datasource_tag}']").click()
        sleep(2)

    def twl_uom_textfield(self, uom):
        self.input_text(TWL_UOM, uom)

    def twl_monitoring_strategy_dropdown(self, strategy):
        self.click_element(TWL_MONITORING_STRATEGY)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{strategy}']").click()
        sleep(2)

    def twl_target_polling_dropdown(self, polling):
        self.click_element(TWL_TARGET_POLLING)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{polling}']").click()
        sleep(2)

    def twl_site_dropdown(self, site):
        self.click_element(TWL_UNIT_DROPDOWN)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{site}']").click()
        sleep(2)

    def twl_section_dropdown(self, section):
        self.click_element(TWL_SECTION_DROPDOWN)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{section}']").click()
        sleep(2)

    def twl_area_dropdown(self, area):
        sleep(2)
        if self.verify_element_is_visible(TWL_AREA_DROPDOWN):
            self.click_element(TWL_AREA_DROPDOWN)
            sleep(2)
            self.spdriver.find_element_by_xpath(f"//*[text()='{area}']").click()
            sleep(2)

    def twl_unit_dropdown(self, unit):
        sleep(2)
        if self.verify_element_is_visible(TWL_UNIT_DROPDOWN):
            self.click_element(TWL_UNIT_DROPDOWN)
            sleep(2)
            self.spdriver.find_element_by_xpath(f"//*[text()='{unit}']").click()
            sleep(2)

    def twl_target_form_dropdown(self, unit):
        sleep(2)
        if self.verify_element_is_visible(TWL_TARGET_FORM_DROPDOWN):
            self.click_element(TWL_TARGET_FORM_DROPDOWN)
            sleep(2)
            self.spdriver.find_element_by_xpath(f"//*[text()='{unit}']").click()
            sleep(2)

    def twl_description_textarea(self, text):
        self.input_text(TWL_DESCRIPTION_TEXTAREA, text)
        sleep(2)

    def twl_click_to_breadcrumb(self):
        if self.verify_element_is_visible(TWL_BREAD_CRUMB):
            self.click_element(TWL_BREAD_CRUMB)

    def twl_verify_message(self, msg):
        twl_msg = self.get_text_of_element(TWL_DESCRIPTION)
        assert twl_msg == msg

    def create_tag_watch_list(self, kwargs):
        try :
            self.navigate_to_tag_watch_list()
            self.twl_click_add_button()
            sleep(20)
            if 'tag' in kwargs:
                self.twl_tag_textfield(kwargs['tag'])
            if 'variable_type' in kwargs:
                self.twl_variable_type_dropdown(kwargs['variable_type'])
            if 'data_type' in kwargs:
                self.twl_data_type_dropdown(kwargs['data_type'])
            if 'datasource' in kwargs:
                self.twl_datasource_dropdown(kwargs['datasource'])
            if 'datasource_tag' in kwargs:
                self.twl_datasource_tag_dropdown(kwargs['datasource_tag'])
            if 'uom' in kwargs:
                self.twl_uom_textfield(kwargs['uom'])
            if 'strategy' in kwargs:
                self.twl_monitoring_strategy_dropdown(kwargs['strategy'])
            if 'polling' in kwargs:
                self.twl_target_polling_dropdown(kwargs['polling'])
            if 'site' in kwargs:
                self.twl_site_dropdown(kwargs['site'])
            if 'section' in kwargs:
                self.twl_section_dropdown(kwargs['section'])
            if 'area' in kwargs:
                self.twl_area_dropdown(kwargs['area'])
            if 'unit' in kwargs:
                self.twl_unit_dropdown(kwargs['unit'])
            if 'target_form' in kwargs:
                self.twl_target_form_dropdown(kwargs['target_form'])
            self.twl_description_textarea(kwargs['message'])
            sleep(5)
            self.click_element(TWL_SAVE_BUTTON)
            sleep(5)
            self.twl_click_to_breadcrumb()
            sleep(5)
            self.twl_verify_message(kwargs['message'])
        except Exception as e:
            attach(data=self.spdriver.get_screenshot_as_png())
            raise(e)