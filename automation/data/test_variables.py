from datetime import datetime

cur_time = str(datetime.time(datetime.now()))
current_time = cur_time.replace(":", "_").replace(".", "_")

log_book_1 = {
    "event_date": "01/08/2021 12:00",
    "status": "Open",
    "category1": "Equipment",
    "priority": "High",
    "site": "Site 1",
    "section": "Section 1",
    "area": "Area 1",
    "unit": "Unit 1",
    "asset_name": "Flare Water Pump",
    "event_msg": "Flare Water Pump",
    "link_url": "https://pilot2019.j5int.com/logbook_standard/view/general_logbook#Lv01/general_logbook",
    "link_desc": "This Logbook Event",
    "filepath": "E:\\Client-code\\automation\\automation\\debug.log"
}


log_book_2 = {
    "event_date": "01/08/2021 12:00",
    "status": "On Hold",
    "category1": "Operations",
    "category2": "Work Instruction",
    "priority": "Critical",
    "site": "Site 2",
    "asset_name": "LPG MRU Bed Vessel",
    "event_msg": "LPG MRU Bed Vessel",
    "link_url": "https://pilot2019.j5int.com/logbook_standard/view/general_logbook#Lv01/general_logbook",
    "link_desc": "This Logbook Event1",
    "filepath": "E:\\Client-code\\automation\\automation\\debug.log"
}


orp1 = {
    "title": f"ORP_01_{current_time}",
    "site": "Site 1",
    "section": "Section 1",
    "area": "Area 1",
    "unit": "Unit 1",
    "round_type": "Maintenance",
    "assigned_group": "Operator",
    "schedule_type": "Simple",
    "duration" : 5,
    "description_text": "ORP_01",
    "sheet_path" : "C:\\Testdata\\Sample Tasks Spreadsheet.xlsx",
    "sheet_upload_confirm" : "yes",
    "static_path" : "C:\\Testdata\\userinput.txt",
    "download_sheet" : "yes"
    }

st_orders_1 = {
    "site": "Site 1",
    "section": "Section 1",
    "area": "Area 1",
    "unit": "Unit 1",
    "renewal_period": 2,
    "renewal_schedule": "Days",
    "file_path": "C:\\Testdata\\userinput.txt",
    "target_group": "select_all",
    "so_msg" : "This is Standing Order Description",
    }

wi_instructions = {
    "status": "In Progress",
    "site": "Site 1",
    "section": "Section 1",
    "area": "Area 1",
    "unit": "Unit 1",
    "category": "Irregular Work",
    "group": "Engineer",
    "task_input": {"desc": "task_01", "comment": "comment_01"},
    "default": 1,
    "start": None,
    "complete": None,
    "filepath": "C:\\Testdata\\count_name.txt",
    "message": "Working Intructions"
}


wp_input = {
    "plan" : "Plan",
    "site": "Site 1",
    "section": "Section 1",
    "area": "Area 1",
    "unit": "Unit 1",
    "category": "Irregular Work",
    "groupname": "Manager",
    "schedule": "Simple",
    "repeat"  : 5,
    "repeat_schedule" : "Hours",
    "duration" : 5,
    "filepath": "C:\\Testdata\\count_name.txt",
    "message": "Working Workplaning"
}

twl_inputs = {
    "tag" : "Tag Watch List1",
    "variable_type" : "Descret",
    "data_type" : "Integer",
    "datasource" : "Default",
    "datasource_tag" : "AV1",
    "uom" : "uom1",
    "status": "In Progress",
    "site": "Site 1",
    "section": "Section 1",
    "area": "Area 1",
    "unit": "Unit 1",
    "category": "Irregular Work",
    "group": "Engineer",
    "task_input": {"desc": "task_01", "comment": "comment_01"},
    "default": 1,
    "start": None,
    "complete": None,
    "filepath": "C:\\Testdata\\count_name.txt",
    "message": "Working Intructions"
}
