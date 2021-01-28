from .browser_actions import BrowserAction
from automation.data.test_data import *
from .locators import *
import pyautogui
from time import sleep
import tenacity as tenacity

class work_instructions(BrowserAction):
    def __init__(self, driver, wait_time):
        super().__init__(driver, wait_time)

    def click_to_operation(self):
        self.click_element(OPERATION_MENU_BUTTON)

    def click_to_working_instructions(self):
        self.click_element(WI_MENU_OPTION)

    def navigate_working_instructions(self, check=None):
        try:
            if check is not None:
                if not self.verify_element_is_visible(WI_HEADER):
                    self.click_to_operation()
                    self.click_to_working_instructions()
                    sleep(5)
                    assert self.verify_element_is_visible(WI_HEADER)
                else:
                    pass
            else:
                self.click_to_operation()
                self.click_to_working_instructions()
                sleep(5)
                assert self.verify_element_is_visible(WI_HEADER)
        except Exception as e:
            self.take_screen_shot('working_instr')
            raise (e)

    def wi_click_add_button(self):
        self.click_element(WI_ADD_BUTTON)

    def wi_select_status_dropdown(self, plan):
        self.click_element(WI_STATUS_DROPDOWN)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{plan}']").click()
        sleep(2)

    def wi_select_site_dropdown(self, site):
        self.click_element(WI_AREA_DROPDOWN)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{site}']").click()
        sleep(2)

    def wi_select_section_dropdown(self, section):
        sleep(2)
        if self.verify_element_is_visible(WI_AREA_DROPDOWN2):
            self.click_element(WI_AREA_DROPDOWN2)
            sleep(2)
            self.spdriver.find_element_by_xpath(f"//*[text()='{section}']").click()
            sleep(2)

    def wi_select_area_dropdown(self, area):
        sleep(2)
        if self.verify_element_is_visible(WI_AREA_DROPDOWN3):
            self.click_element(WI_AREA_DROPDOWN3)
            sleep(2)
            self.spdriver.find_element_by_xpath(f"//*[text()='{area}']").click()
            sleep(2)

    def wi_select_unit_dropdown(self, unit):
        sleep(2)
        if self.verify_element_is_visible(WI_AREA_DROPDOWN4):
            self.click_element(WI_AREA_DROPDOWN4)
            sleep(2)
            self.spdriver.find_element_by_xpath(f"//*[text()='{unit}']").click()
            sleep(2)

    def wi_category_dropdown(self, category):
        self.click_element(WI_CATEGORY_DROPDOWN)
        sleep(2)
        self.input_text(WI_CATEGORY_TEXTBOX, category)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{category}']").click()
        sleep(2)

    def wi_assigned_group(self, groupname):
        self.click_element(WI_ASSIGNED_GROUP_DROPDOWN)
        sleep(2)
        self.spdriver.find_element_by_xpath(f"//*[text()='{groupname}']").click()
        sleep(2)

    def click_start_done_button(self):
        self.click_element(WI_START_DONE_BUTTON)

    def click_complete_done_button(self):
        self.click_element(WI_COMPLETE_DONE_BUTTON)

    def wi_task_description(self, input, default=1, start=None, complete=None):
        if default == 1:
            self.input_text(WI_TASK_DESCRIPTION_FIELD, input['desc'])
            self.input_text(WI_TASK_COMMENT_FIELD, input['comment'])
        elif default > 1 :
            for j in range(1, default):
                self.click_element(WI_ADD_WORK_FILED_BUTTON)
            for i in range(1, default+1):
                wi_desc = f"(//td[contains(@class,'TaskDescription')]//input[@class='FormInput'])[{i}]"
                wi_comnt = f"(//td[contains(@class,'TaskDoneComment')]//input[@class='FormInput'])[{i}]"
                self.input_text((XPATH, wi_desc), input[i]['desc'])
                self.input_text((XPATH, wi_comnt), input[i]['comment'])
        if start is not None:
            self.click_start_done_button()
        else:
            pass

        if complete is not None:
            self.click_complete_done_button()
        else:
            pass

    def wi_message_box(self, message):
        self.switch_to_iframe(WI_MESSAGE_IFRAME)
        sleep(2)
        self.input_text(WI_MESSAGE_BOX_ID, message)
        sleep(2)
        self.switch_to_default()
        sleep(2)
        self.switch_to_iframe(WI_IFRAME)

    def wi_start_time(self, start_time):
        self.input_text(WI_START_DATE_TIME, start_time)

    def wi_finish_time(self, finish_time):
        self.input_text(WI_END_DATE_TIME, finish_time)

    def wi_upload_file(self, filepath):
        sleep(2)
        self.spdriver.find_element_by_name(WI_UPLOAD_FILE[1]).send_keys(filepath)
        sleep(2)

    def create_work_instruction(self, kwargs):
        self.navigate_working_instructions()
        self.wi_click_add_button()
        sleep(20)
        self.switch_to_iframe(WI_IFRAME)
        if 'status' in kwargs:
            self.wi_select_status_dropdown(kwargs['status'])
        if 'start_time' in kwargs:
            self.wi_start_time(kwargs['start_time'])
        if 'finish_time' in kwargs:
            self.wi_finish_time(kwargs['finish_time'])
        if 'site' in kwargs:
            self.wi_select_site_dropdown(kwargs['site'])
        if 'section' in kwargs:
            self.wi_select_section_dropdown(kwargs['section'])
        if 'area' in kwargs:
            self.wi_select_area_dropdown(kwargs['area'])
        if 'unit' in kwargs:
            self.wi_select_unit_dropdown(kwargs['unit'])
        if 'category' in kwargs:
            self.wi_category_dropdown(kwargs['category'])
        if 'group' in kwargs:
            self.wi_assigned_group(kwargs['group'])
        if 'task_input' in kwargs:
            self.wi_task_description(kwargs['task_input'], kwargs['default'], kwargs['start'], kwargs['complete'])
        if 'filepath' in kwargs:
            self.wi_upload_file(kwargs['filepath'])
        self.wi_message_box(kwargs['message'])
        self.click_element(WI_SAVE_BUTTON)



