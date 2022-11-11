#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-10-31 9:22 p.m.
# Author: Ding
from time import sleep
from typing import Type, Union

# import different browser and their options
from selenium.webdriver import *

import settings


class BrowserTypeError(Exception):
    def __init__(self, _type):
        self._type = _type

    def __str__(self):
        return f'unsupported browser type'


class Browser:
    chrome_driver_path = settings.CHROME_DRIVER_PATH
    firefox_driver_path = settings.FIREFOX_DRIVER_PATH
    edge_driver_path = settings.EDGE_DRIVER_PATH
    ie_driver_path = settings.IE_DRIVER_PATH
    # wind size
    windows_size = settings.WINDOW_SIZE
    # wait time
    implicit_time = settings.IMPLICITLY_WAIT_TIME
    # page load time
    page_load_time = settings.PAGE_LOAD_TIME
    # javascript execution time
    script_time_out = settings.SCRIPT_TIMEOUT
    # default headless
    headless = settings.HEADLESS

    def __init__(self, browser_type: Type[Union[Chrome, Ie, Edge, Firefox, Safari]] = Chrome,
                 option_type: Type[Union[ChromeOptions, FirefoxOptions, IeOptions]] = ChromeOptions,
                 driver_path: str = chrome_driver_path):

        if not issubclass(browser_type, (Chrome, Ie, Edge, Firefox, Safari)):
            raise BrowserTypeError(browser_type)
        if not issubclass(option_type, (ChromeOptions, FirefoxOptions, IeOptions)):
            raise BrowserTypeError(option_type)
        if not isinstance(driver_path, str):
            raise TypeError

        self._path = driver_path
        self._browser = browser_type
        self._option = option_type

    @property
    def options(self):
        """
        browser options implemented by subclass
        :return:
        """
        return

    @property
    def browser(self):
        """
        return a browser instance implemented by subclass
        :return:
        """
        return


class ChromeBrowser(Browser):
    # add option mark to use default options or customized options
    option_mark = settings.CHROME_OPTION_MARK
    # config the browser after it starts
    method_mark = settings.CHROME_METHOD_MARK

    # override base class Browser attribute
    headless = settings.CHROME_HEADLESS
    page_load_time = settings.CHROME_PAGE_LOAD_TIME
    script_time_out = settings.SCRIPT_TIMEOUT
    windows_size = settings.WINDOW_SIZE

    arguments = settings.CHROME_ARGUMENTS

    experiment = settings.CHROME_EXPERIMENTAL

    @property
    def options(self):
        if self.option_mark:
            chrome_option = self._option()

            for args in self.arguments:
                chrome_option.add_argument(args)

            for k, v in self.experiment.items():
                chrome_option.add_experimental_option(k, v)
            chrome_option.headless = self.headless

            return chrome_option
        else:
            return None

    @property
    def browser(self):
        if self.options:  # set options for browser before it starts
            chrome = self._browser(self._path, options=self.options)
        else:  # default option for browser
            chrome = self._browser(self._path)

        if self.method_mark:  # set actions after the browser started
            chrome.implicitly_wait(self.implicit_time)
            chrome.set_script_timeout(self.script_time_out)
            chrome.set_page_load_timeout(self.page_load_time)
            chrome.delete_all_cookies()
            chrome.set_window_size(*self.windows_size)

        return chrome


class IEBrowser(Browser):
    clean_session = True

    def __init__(self):
        super().__init__(
            browser_type=Ie,
            option_type=IeOptions,
            driver_path=super().ie_driver_path
        )

    @property
    def options(self):
        ie_option = self._option()
        ie_option.ensure_clean_session = self.clean_session

        return ie_option

    @property
    def browser(self):
        ie = self._browser(self._path, options=self.options)
        ie.implicitly_wait(self.implicit_time)
        ie.set_page_load_timeout(self.page_load_time)
        ie.set_script_timeout(self.script_time_out)
        ie.maximize_window()
        return ie


if __name__ == '__main__':
    with ChromeBrowser().browser as _chrome:
        # _chrome.get('http://www.amazon.ca')
        _chrome.get('https://www.saucedemo.com/')
        sleep(2)
