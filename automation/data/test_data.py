import os

browser = 'chrome'
product_url = str("https://pilot2019.j5int.com")
Username="j5qademo"
Password="biosphere_novel_gazette"
search_value = "Selenium"
wait_time = 60
headless = "false"

LOG_DIR = os.path.join(os.getcwd(), 'log')

IMAGE_DIR= os.path.join(os.getcwd(), 'images')
if os.path.isdir(IMAGE_DIR):
    pass
else:
    os.mkdir(IMAGE_DIR)

driver_path = os.path.join(os.getcwd(), 'driver')
chrome_driver_path = os.path.join(driver_path, 'chromedriver.exe')
firefox_driver_path = os.path.join(driver_path, 'geckodriver.exe')
edge_driver_path = os.path.join(driver_path, 'msedgedriver.exe')

download_path = "C:\\Users\\Deepesh Yadav\\Downloads\\"