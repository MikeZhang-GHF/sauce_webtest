#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-10 3:22 p.m.
# Author: Ding
import datetime
import os

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

import settings


# PO pattern
class BasePage:
    """
    Base class for all the page objects.
    """

    url = settings.SAUCE_PROJECT
    locators = {}

    def __init__(self, driver: WebDriver):
        if not driver:
            raise Exception("driver must be the instance of WebDriver")
        self._driver = driver

    @property
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self, driver: WebDriver):
        """set to different driver to test different browser compatibility"""
        if not driver:
            raise Exception("driver must be the instance of WebDriver")
        self._driver = driver

    def __getattr__(self, locator):
        """set locators as attributes"""
        if locator not in self.locators:
            raise Exception("locator does not exist.")
        return self.locators[locator]

    def _init_wait(self, timeout, poll_frequency):
        """explicit wait for elements on page"""
        if timeout is None:
            timeout = settings.UI_TIME_OUT
        if poll_frequency is None:
            poll_frequency = settings.POLL_FREQUENCY

        return WebDriverWait(driver=self._driver, timeout=timeout, poll_frequency=poll_frequency)

    def _find_element_condition(self, locator, timeout=None, poll_frequency=None,
                                condition="visibility_of_element_located"):
        """find element based on different condition using reflection"""
        try:
            return self._init_wait(timeout, poll_frequency). \
                until(getattr(ec, condition)(locator))
        except TimeoutException:
            self._driver.quit()
            raise TimeoutException(f"{locator}: locate element failed!")

    def find_element_visible(self, locator, timeout=None, poll_frequency=None):
        """wait for the UI element until it is visible on web page"""
        return self._find_element_condition(locator, timeout, poll_frequency)

    def find_element_presence(self, locator, timeout=None, poll_frequency=None):
        """wait for the UI element until it presents in the DOM"""
        return self._find_element_condition(locator, timeout, poll_frequency, "presence_of_element_located")

    def find_element_clickable(self, locator, timeout=None, poll_frequency=None):
        """wait for the UI element until it is clickable"""
        return self._find_element_condition(locator, timeout, poll_frequency, "element_to_be_clickable")

    def get(self, url=None):
        """go to the url"""
        if url:
            self.url = url
        self._driver.get(self.url)

    def close(self):
        self._driver.quit()

    def click(self, locator):
        """click the UI element"""
        element = self.find_element_clickable(locator)
        element.click()

    def send_keys(self, locator, keys):
        """input value in the UI input element"""
        element = self.find_element_visible(locator)
        element.clear()
        element.send_keys(keys)

    def get_text(self, locator):
        """get the text of the element"""
        return self.find_element_visible(locator).text

    def switch_into_frame(self, locator):
        """switch to the iframe on page"""
        iframe = self.find_element_visible(locator)
        return self._driver.switch_to.frame(iframe)

    def switch_from_frame_to_content(self):
        """switch back from iframe to main page"""
        return self._driver.switch_to.parent_frame()

    def switch_window_to_last_handle(self):
        """switch to the last page for the multiple pages scenario"""
        window_handles = self._driver.window_handles
        self._driver.switch_to.window(window_handles[-1])

    def switch_to_default_content(self):
        """switch back to the first page for the multiple pages scenario"""
        self._driver.switch_to.default_content()

    def upload(self, locator, file_path):
        """upload file from user browser"""
        element = self.find_element_presence(locator)
        return element.send_keys(file_path)

    def scroll_to_element(self, locator):
        """scroll to the element by execute javascript"""
        element = self.find_element_presence(locator)
        self._driver.execute_script("arguments[0].scrollIntoView(false)", element)
        return True

    def element_is_displayed(self, locator, timeout=30):
        """check if an element is displayed"""
        self.find_element_visible(locator, timeout)

    def element_screenshot(self, locator):
        """screenshot for the web element"""
        ele_img_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".png"
        ele_img_dir_path = settings.SCREENSHOT_ELEMENT_DIR
        if not os.path.exists(ele_img_dir_path):
            os.mkdir(ele_img_dir_path)
        ele_img_path = os.path.join(ele_img_dir_path, ele_img_name)
        self.find_element_visible(locator).screenshot(ele_img_path)
        return ele_img_path
