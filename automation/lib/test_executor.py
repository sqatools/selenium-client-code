import os, sys
from datetime import datetime
#from automation.data.test_data import headless

userinput = sys.argv[1]

cur_wd = os.getcwd()
cur_time = str(datetime.time(datetime.now()))
current_time = cur_time.replace(":", "_").replace(".", "_")
report_file = f"report_{current_time}.html"
#cmd = f"pytest -v -s test_cases\\test_smoke.py  --html-report=./report/{report_file}"

if userinput == 'smoke':
    cmd = f"pytest -v -s test_cases\\test_smoke.py  --html-report=./report/{report_file}"
    os.system(cmd)
elif userinput == 'sanity':
    cmd = f"pytest -v -s test_cases\\test_sanity.py  --html-report=./report/{report_file}"
    os.system(cmd)
else:
    print("There is such test suite", userinput)

