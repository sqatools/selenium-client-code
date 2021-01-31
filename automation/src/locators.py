from selenium.webdriver.common.by import By
from automation.data.test_variables import *

XPATH = By.XPATH
NAME = By.NAME
CSS = By.CSS_SELECTOR
ID = By.ID
LINKTEXT = By.LINK_TEXT

GOOGLE_SEARCH_BOX = (NAME, "q")
GOOGLE_SEARCH_BUTTON = (NAME, "btnK")

LOGIN_USERNAME = (ID, "username_input")
LOGIN_PASSWORD = (ID, "password_input")
LOGIN_BUTTON= (ID, "login_label")
LOGIN_TERMS_CHECKBOX = (ID, "terms_checkbox")

APPLICATION_HOME_PAGE_NAV = (XPATH, "//h1[text()='Application Navigation']")

OPERATION_MENU_BUTTON = (ID, "j5_OperationsLogbook_OperationsMenu_node")
LOGBOOK_MENU_OPTION = (XPATH, "//td[contains(@id,'dijit_MenuItem')]//a[text()='Operations Logbook']")
LOGBOOK_HEADER = (XPATH, "//span[text()='Operations Logbook']")

LOGBOOK_DETAIL_TAB = (XPATH, "//span[text()='Detail']")
ADD_LOGBOOK_ENTRY = (XPATH, "(//a[contains(@id,'j5_MainFormAddControl')])[1]")
CALENDER_SELECT_BUTTON = (XPATH, "//*[@aria-label='Select date']")
CAL_MONTH_LABEL = (ID, "rw_1_date_calendar_label")
CAL_INPUT_BOX = (ID, "rw_1_input")

LOOG_BOOK_FRAME = (XPATH, "//iframe[contains(@src,'general_logbook')]")
STATUS_DROP_DOWN = (XPATH, "//span[text()='Status']//ancestor::td//following-sibling::td[1]//div[contains(@class, 'is-searchable')]")

CATEGORY_DROP_DOWN1 = (XPATH, "//span[text()='Category']//ancestor::td//following-sibling::td[1]//span[@class='Select-arrow-zone']")
CATEGORY_TEXT_BOX = (XPATH, "//span[text()='Category']//ancestor::td//following-sibling::td[1]//input[@role='combobox']")
CATEGORY_DROP_DOWN_ELEMENT = (XPATH, "//div[@class='Select-menu-outer']//*")

CATEGORY_DROP_DOWN2 = (XPATH, "(//span[text()='Category']//ancestor::td//following-sibling::td[1]//span[@class='Select-arrow-zone'])[2]")
CATEGORY_TEXT_BOX2 =  (XPATH,"(//span[text()='Category']//ancestor::td//following-sibling::td[1]//input[@role='combobox'])[2]")

PRIORITY_DROP_DOWN = (XPATH, "//span[text()='Priority']//ancestor::td//following-sibling::td[1]//span[@class='Select-arrow-zone']")

LOG_BOOK_AREA_DROP_DOWN = (XPATH, "//span[text()='Area']//ancestor::td//following-sibling::td[1]//span[@class='Select-arrow-zone']")

LOG_BOOK_AREA_DROP_DOWN2 = (XPATH, "(//span[text()='Area']//ancestor::td//following-sibling::td[1]//span[@class='Select-arrow-zone'])[2]")

LOG_BOOK_AREA_DROP_DOWN3 = (XPATH, "(//span[text()='Area']//ancestor::td//following-sibling::td[1]//span[@class='Select-arrow-zone'])[3]")

LOG_BOOK_AREA_DROP_DOWN4 = (XPATH, "(//span[text()='Area']//ancestor::td//following-sibling::td[1]//span[@class='Select-arrow-zone'])[4]")

EQUIPMENT_BUTTON = (XPATH, "//span[text()='Equipment']//ancestor::td//following-sibling::td[1]//button")

ASSET_SEARCH_BOX = (NAME, "asset-selector-modal-search")

CONFIRM_BUTTON = (XPATH, "//button[text()='Confirm']")

TEXT_AREA_IFRAME_ID = (ID, "react-tinymce-0_ifr")

TEXT_FIELD_ID = (ID, "tinymce")
DROP_FILE_INITIATE_BUTTON = (XPATH, "//div[@class='InputGroup_section']/button")

ATTACHMENT_LINK_TEXTBOX = (NAME, "horizontal-form-input-link")
LINK_DESCRIPTION_TEXT_BOX = (NAME, "horizontal-form-input-link-desc")
ADD_LINK_BUTTON  = (XPATH, "//button[text()='Add link']")

DRAG_DROP_FILE_TO_UPLOAD = (XPATH, "(//div[@class='FileDragAndDrop FileDragAndDrop__label'])[2]")
SAVE_BUTTON = (XPATH, "//span[text()='Save']//parent::button")

LOOG_BOOK_BREDCRUM = (XPATH, "//a/span[@class='crumb-token' and contains(text(), 'Operations Logbook')]")

RECENTLY_ADDED_LOGBOOK_TIME = (XPATH, "(//tbody[contains(@id,'row_general_logbook')])[1]//td[@class='general_logbook-start_time-header-cell-class']//div")
RECENTLY_ADDED_LOGBOOK_MSG = (XPATH, "//table[contains(@id, 'general_logbook_table')]//tbody[contains(@id, 'row_general_logbook')][1]/tr/td[contains(@class, 'logbook-message')]/div")

################ Operator Round Planing ###############
 
ORP_MENU_OPTION  = (XPATH, "//td[contains(@id,'dijit_MenuItem')]//a[text()='Operator Rounds Planning']")
ORP_HEADER = (XPATH, "//span[text()='Operator Rounds Planning']")
ADD_BUTTON = (XPATH, "(//a[contains(@id,'j5_ViewReplaceLink') and text()='Add'])[1]")
ORP_TITLE = (XPATH, "//input[contains(@id, 'dijit_form_ValidationTextBox_1')]")
ORP_SITE_DROPDOWN = (XPATH, "//td[contains(text(), 'Site')]//following-sibling::td//span[contains(@id, 'operator_rounds_plan')]")
ORP_SECTION_DROPDOWN = (XPATH, "//td[contains(text(), 'Section')]//following-sibling::td//span[contains(@id, 'operator_rounds_plan')]")
ORP_AREA_DROPDOWN = (XPATH, "//td[contains(text(), 'Area')]//following-sibling::td//span[contains(@id, 'operator_rounds_plan')]")
ORP_UNIT_DROPDOWN = (XPATH, "//td[contains(text(), 'Unit')]//following-sibling::td//span[contains(@id, 'operator_rounds_plan')]")
ORP_ROUND_TYPE_DROPDOWN = (XPATH, "//td[contains(text(), 'Round Type')]//following-sibling::td//span[contains(@id, 'operator_rounds_plan')]")
ORP_ASSIGNED_GROUP_DROPDOWN = (XPATH, "//td[contains(text(), 'Assigned Group')]//following-sibling::td//div[contains(@id, 'operator_rounds_plan')]")
ORP_SCHEDULED_TYPE_DROPDOWN = (XPATH, "//td[contains(text(), 'Schedule Type')]//following-sibling::td[contains(@class, 'schedule_type')]/div")
ORP_START_DATE = (XPATH, "//td[contains(text(), 'Start Time')]//following-sibling::td//input[contains(@id,'DateTime_Calendar')]")
ORP_START_TIME = (XPATH, "//td[contains(text(), 'Start Time')]//following-sibling::td//input[contains(@id,'DateTime_TimePicker')]")
ORP_FINISH_DATE = (XPATH, "//td[contains(text(), 'Finish Time')]//following-sibling::td//input[contains(@id,'DateTime_Calendar')]")
ORP_FINISH_TIME = (XPATH, "//td[contains(text(), 'Finish Time')]//following-sibling::td//input[contains(@id,'DateTime_TimePicker')]")
ORP_TIMEZONE_DROPDOWN = (XPATH, "//td[contains(text(), 'Timezone')]//following-sibling::td//div[contains(@id,'schedule_timezone')]")
ORP_TIMEZONE_TEXTFIELD = (XPATH, "//td[contains(text(), 'Timezone')]//following-sibling::td//input[contains(@id,'schedule_timezone')]")
ORP_REPEAT_EVERY_TEXT_FIELD = (XPATH, "//td[contains(text(), 'Repeat Every')]//following-sibling::td//input[contains(@id,'dijit_form_NumberTextBox')]")
ORP_REPEAT_EVERY_DROP_DOWN = (XPATH, "//td[contains(text(), 'Repeat Every')]//following-sibling::td[contains(@class,'repeat_period-field')]/div")
ORP_ADDITIONAL_DATES = (XPATH, "//td[contains(text(), 'Additional Dates')]//following-sibling::td//input[contains(@id,'dijit_form_ValidationTextBox')]")
ORP_EXCLUDED_DATES = (XPATH, "//td[contains(text(), 'Excluded Dates')]//following-sibling::td//input[contains(@id, 'dijit_form_ValidationTextBox')]")
ORP_DURATION = (XPATH, "//td[contains(text(), 'Duration')]//following-sibling::td//input[contains(@id, 'dijit_form_NumberTextBox')]")
ORP_TEXT_FIELD_IFRAME = (XPATH, "//iframe[contains(@id, 'newrow_operator_rounds_plan')]")
ORP_BODY_TEXT= (ID, "tinymce")
ORP_SAVE_BUTTON = (XPATH, "//a[contains(@submitform, 'newrow_operator_rounds_plan')]")

ORP_UPLOAD_TASK_SPREADSHEET = (XPATH, "//span[text()='Upload Tasks Spreadsheet']")
ORP_UPLOAD_STATIC_FILE = (XPATH, "//span[text()='Upload Static File']")
ORP_CHOOSE_UPLOAD_FILE = (NAME, "file_input")
ORP_CONFIRM_UPLOAD_BUTTON = (XPATH, "//span[text()='Confirm']")
ORP_CANCEL_ULOAD_BUTTON = (XPATH, "//span[text()='Cancel']")
ORP_DOWNLOAD_TASKS_SPREADSHEET = (XPATH, "//span[text()='Download Tasks Spreadsheet']")

ORP_CANCEL_BUTTON = (XPATH, "//a[contains(@id, 'j5_ViewReplaceLink')]")
ORP_BREAD_CRUMP = (XPATH, "//div[@id='j5Breadcrumb']//a/span[text()='Operator Rounds Planning']")
OPR_TITLE_HEADER = (XPATH, "(//td[contains(@class,'title-header-cell')]/div)[1]")

############## Standing Orders ##############

SO_MENU_OPTION = (XPATH, "//td[contains(@id,'dijit_MenuItem')]//a[text()='Standing Orders']")
SO_HEADER = (XPATH, "//span[text()='Standing Orders']")
SO_ADD_BUTTON = (XPATH, "(//a[contains(@id,'j5_ViewReplaceLink') and text()='Add'])[1]")
SO_SITE_DROPDOWN = (XPATH, "//td[contains(text(), 'Site')]//following-sibling::td//span[contains(@id, 'standing_orders_view')]")
SO_SECTION_DROPDOWN = (XPATH, "//td[contains(text(), 'Section')]//following-sibling::td//span[contains(@id, 'standing_orders_view')]")
SO_AREA_DROPDOWN = (XPATH, "//td[contains(text(), 'Area')]//following-sibling::td//span[contains(@id, 'standing_orders_view')]")
SO_UNIT_DROPDOWN = (XPATH, "//td[contains(text(), 'Unit')]//following-sibling::td//span[contains(@id, 'standing_orders_view')]")
SO_START_DATE = (XPATH, "(//input[contains(@id, 'DateTimePicker_0')])[1]")
SO_START_TIME = (XPATH, "(//input[contains(@id, 'DateTimePicker_0')])[2]")
SO_END_DATE = (XPATH, "(//input[contains(@id, 'DateTimePicker_1')])[1]")
SO_END_TIME = (XPATH, "(//input[contains(@id, 'DateTimePicker_1')])[2]")
SO_RENEWAL_PERIOD = (XPATH, "//input[contains(@id,'dijit_form_NumberTextBox')]")
SO_RENEWAL_SCHEDULE = (XPATH, "//td[contains(text(), 'Acknowledgement Renewal Period')]//parent::tr/td[3]/div")
SO_ATTACHMENT_BUTTON = (XPATH, "//a[contains(text(), 'Add an attachment ...')]")
SO_UPLOAD_IFRAME = (XPATH, "//iframe[contains(@id, 'standing_orders_view_attachment')]")
SO_BROWSE_BUTTON = (NAME, "filedata")
SO_EMAIL_TARGET_CHECKBOX = (XPATH, "//td[contains(text(), 'Email Target')]//following::input[contains(@id,'dijit_form_CheckBox')]")
SO_SELECT_ALL_TARGET_GROUP = (XPATH, "//span[text()='Select All']")
SO_SELECT_NONE_TARGET_GROUP = (XPATH, "//span[text()='Select None']")
SO_SELECT_INVERT_TARGET_GROUP = (XPATH, "//span[text()='Invert Selection']")
SO_SELECT_SPECIFIC_TARGET_GROUP= (ID, "//div[text()='Manager']//parent::div//input[contains(@id,'dijit_form_CheckBox')]")
SO_SELECT_STATUS = (XPATH, "//td[contains(text(),'Status')]//following-sibling::td//tr")
SO_SAVE_BUTTON = (XPATH, "//a[contains(@submittarget,'newrow_standing_orders')]")
SO_BODY_TEXT= (ID, "tinymce")
SO_IFRAME_XPATH = (XPATH, "//iframe[contains(@id, 'newrow_standing_orders')]")
SO_ORDER = (XPATH, "//tbody[contains(@id,'row_standing_orders')]/tr[1]/td[3]/div")
SO_BREAD_CRUMB = (XPATH, "//div[@id='j5Breadcrumb']//a/span[text()='Standing Orders']")

##############  Work Instructions ##############

WI_ADD_BUTTON = (XPATH, "//a[contains(@id,'j5_MainFormAddControl_1') and text()='Add']")
WI_MENU_OPTION = (XPATH, "//td[contains(@id,'dijit_MenuItem')]//a[text()='Work Instructions']")
WI_HEADER = (XPATH, "//span[text()='Work Instructions']")
WI_IFRAME = (XPATH, "//iframe[contains(@src, 'serve_add_form')]")
WI_STATUS_DROPDOWN = (XPATH, "//td//span[text()='Status']//ancestor::td//following-sibling::td//div[@class='Select-control']")
WI_START_DATE_TIME = (XPATH, "(//div[contains(@class, 'rw-datetime-picker')]//input)[1]")
WI_END_DATE_TIME = (XPATH, "(//div[contains(@class, 'rw-datetime-picker')]//input)[2]")
WI_AREA_DROPDOWN = (XPATH, "//span[text()='Area']//ancestor::td//following-sibling::td//div[@class='Select-control']")
WI_AREA_DROPDOWN2 = (XPATH, "(//span[text()='Area']//ancestor::td//following-sibling::td//div[@class='Select-control'])[2]")
WI_AREA_DROPDOWN3 = (XPATH, "(//span[text()='Area']//ancestor::td//following-sibling::td//div[@class='Select-control'])[3]")
WI_AREA_DROPDOWN4 = (XPATH, "(//span[text()='Area']//ancestor::td//following-sibling::td//div[@class='Select-control'])[4]")
WI_CATEGORY_DROPDOWN = (XPATH, "//span[text()='Category']//ancestor::td//following-sibling::td//div[@class='Select-control']")
WI_CATEGORY_TEXTBOX = (XPATH, "//span[text()='Category']//ancestor::td//following-sibling::td//div[@class='Select-control']//input")
WI_ASSIGNED_GROUP_DROPDOWN = (XPATH, "//span[text()='Assigned Group']//ancestor::td//following-sibling::td//div[@class='Select-control']")
WI_TASK_DESCRIPTION_FIELD = (XPATH, "//td[contains(@class,'TaskDescription')]//input[@class='FormInput']")
WI_TASK_COMMENT_FIELD = (XPATH, "//td[contains(@class,'TaskDoneComment')]//input[@class='FormInput']")
WI_ADD_WORK_FILED_BUTTON = (XPATH, "//td[contains(@class,'repeating-section')]/div[contains(@class,'instance-add-button')]")
WI_START_DONE_BUTTON = (XPATH, "//span[text()='Start Work']//ancestor::td//following-sibling::td//button[text()='Done']")
WI_COMPLETE_DONE_BUTTON = (XPATH, "//span[text()='Complete Work']//ancestor::td//following-sibling::td//button[text()='Done']")
WI_MESSAGE_IFRAME = (ID, "react-tinymce-0_ifr")
MESSAGE_BOX_ID = (ID, "tinymce")
WI_UPLOAD_FILE = (XPATH, "//div[contains(@class,'FileDragAndDrop')]/input")
WI_SAVE_BUTTON = (XPATH, "//span[text()='Save']//parent::button")
WI_CANCEL_BUTTON = (XPATH, "//span[text()='Cancel']//parent::button")
WI_BREAD_CRUMB = (XPATH, "//a/span[@class='crumb-token' and contains(text(), 'Work Instructions')]")
WI_DESCRIPTION_MESSAGE = (XPATH, "//table[@id='work_overview_table']//tbody[contains(@id, 'row_work_overview')][1]//td[contains(@class, 'description')]/div")

####################  Work Planning #################

WP_MENU_OPTION = (XPATH, "//td[contains(@id,'dijit_MenuItem')]//a[text()='Work Planning']")
WP_HEADER = (XPATH, "//span[text()='Work Planning']")
WP_ADD_BUTTON = (XPATH, "(//a[contains(@id,'j5_ViewReplaceLink') and text()='Add'])[1]")
WP_PLAN_TEMPLATE_DROPDOWN = (XPATH, "//td[contains(text(), 'Plan/Template')]//following-sibling::td//tr")
WP_SITE_DROPDOWN = (XPATH, "//td[contains(text(), 'Site')]//following-sibling::td//tr")
WP_SECTION_DROPDOWN = (XPATH, "//td[contains(text(), 'Section')]//following-sibling::td//tr")
WP_AREA_DROPDOWN = (XPATH, "//td[contains(text(), 'Area')]//following-sibling::td//tr")
WP_UNIT_DROPDOWN = (XPATH, "//td[contains(text(), 'Unit')]//following-sibling::td//tr")
WP_WORK_CATEGORY_DROPDOWN = (XPATH, "//td[contains(text(), 'Work Category')]//following-sibling::td//tr")
WP_ASSIGNED_GROUP_DROPDOWN = (XPATH, "//td[contains(text(), 'Assigned Group')]//following-sibling::td//tr")
WP_INDUSTRFORM_DROPDOWN = (XPATH, "//td[contains(text(), 'IndustraForm')]//following-sibling::td/div/div[contains(@id, 'scheduled_work_viewtop')]")
WP_SCHEDULE_TYPE = (XPATH, "//td[contains(text(), 'Schedule Type')]//following-sibling::td//table[contains(@id, 'j5_UpdatingSelect')]//tr")
WP_START_DATE = (XPATH, "//td[contains(text(), 'Start Time')]//following-sibling::td//div[contains(@id, 'widget_DateTime_Calendar')]")
WP_START_TIME = (XPATH, "//td[contains(text(), 'Start Time')]//following-sibling::td//div[contains(@id, 'widget_DateTime_TimePicke')]")
WP_FINISH_DATE = (XPATH, "//td[contains(text(), 'Finish Time')]//following-sibling::td//div[contains(@id, 'widget_DateTime_Calendar')]")
WP_FINISH_TIME = (XPATH, "//td[contains(text(), 'Finish Time')]//following-sibling::td//div[contains(@id, 'widget_DateTime_TimePicke')]")
WP_TIMEZONE = (XPATH, "//td[contains(text(), 'Timezone')]//following-sibling::td//div[contains(@id,'schedule_timezone')]")
WP_TIMEZONE_TEXTFIELD = (XPATH, "//td[contains(text(), 'Timezone')]//following-sibling::td//input[contains(@id,'schedule_timezone')]")
WP_ADD_ATTACHMENT = (XPATH, "//a[contains(text(), 'Add an attachment ...')]")
WP_BROWSER = (NAME, "filedata")
WP_MESSAGE_IFRAME = (XPATH, "//iframe[contains(@id, 'newrow_scheduled_work')]")
WP_SAVE_BUTTON = (XPATH, "//div[contains(@id, 'j5_Actions_1')]//a[contains(text(), 'Save')]")
WP_BREAD_CRUMB = (XPATH, "//a/span[@class='crumb-token' and contains(text(), 'Work Planning')]")
WP_DESCRIPTION_MSG = (XPATH, "//table[@id='scheduled_work_table']//tbody[contains(@id, 'row_scheduled_work')][1]//td[contains(@class, 'description')]/div")