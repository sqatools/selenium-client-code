from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from automation.data.test_data import *
import logging
import os
from datetime import datetime


logging.basicConfig(filename=os.path.join(LOG_DIR, "master.log"), level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)


class BrowserAction():
      def __init__(self, driver, wait_time):
          self.spdriver = driver
          self.wait = WebDriverWait(self.spdriver, wait_time)

      def click_element(self, selector):
          element = self.wait.until(EC.presence_of_element_located(selector))
          logger.debug(f"This the element on which click action would be performed : {selector}")
          element.click()

      def input_text(self, selector, value):
          logger.debug(f"This the element on which will put new data : {selector}")
          element = self.wait.until(EC.presence_of_element_located(selector))
          element.clear()
          element.send_keys(value)
          logger.info(f"Input : {value}, provide to this element : {selector}")

      def verify_element_is_visible(self, selector):
          try:
              logger.debug(f" will verify visibility of given element;  {selector} ")
              self.wait.until(EC.visibility_of_element_located(selector))
              logger.info(f"Element varified successfully : {selector}")
              return True
          except:
              return False

      def take_screen_shot(self, prefix):
          cur_time = str(datetime.time(datetime.now()))
          current_time = cur_time.replace(":", "_").replace(".", "_")
          filename = f"{prefix}_{current_time}.png"
          if os.path.isdir(IMAGE_DIR):
              self.spdriver.save_screenshot(os.path.join(IMAGE_DIR, filename))
          else:
              os.mkdir(IMAGE_DIR)
              self.spdriver.save_screenshot(os.path.join(IMAGE_DIR, filename))

      def get_all_elements(self, selector):
          elements = self.wait.until(EC.presence_of_all_elements_located(selector))
          return elements

      def get_text_of_element(self, selector):
          element = self.wait.until(EC.presence_of_element_located(selector))
          return element.text

      def launch_url(self, url):
          self.spdriver.get(str(url))
          logger.info(f"Given URL : {url}")


      def switch_to_iframe(self, selector):
          element = self.wait.until(EC.presence_of_element_located(selector))
          self.spdriver.switch_to.frame(element)

      def switch_to_default(self):
           self.spdriver.switch_to.default_content()

      def check_element_is_enabled(self, selector):
          self.wait.until(EC.element_to_be_clickable(selector))

      def get_attribute_value(self, selector, attribute):
          element = self.wait.until(EC.presence_of_element_located(selector))
          attrib_value = element.get_attribute(attribute)
          return attrib_value


