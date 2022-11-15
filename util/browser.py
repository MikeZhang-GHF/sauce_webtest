#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-10-31 9:22 p.m.
# Author: Ding
from time import sleep
from typing import Type, Union

# import different browser and their options
from selenium.webdriver import Chrome, ChromeOptions, Firefox, FirefoxOptions, Edge, EdgeOptions, Safari
from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager

# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
import settings


class BrowserTypeError(Exception):
    def __init__(self, _type):
        self._type = _type

    def __str__(self):
        return f'unsupported browser type'


class Browser:
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
    # webdriver manager download matched webdriver for browser
    service = None

    def __init__(self, browser_type: Type[Union[Chrome, Firefox, Edge, Safari]] = Chrome,
                 option_type: Type[Union[ChromeOptions, FirefoxOptions, EdgeOptions]] = ChromeOptions):

        if not issubclass(browser_type, (Chrome, Edge, Firefox, Safari)):
            raise BrowserTypeError(browser_type)
        if not issubclass(option_type, (ChromeOptions, FirefoxOptions, EdgeOptions)):
            raise BrowserTypeError(option_type)

        self._browser = browser_type
        self._option = option_type

    @property
    def options(self):
        """browser options implemented by subclass"""
        return

    @property
    def browser(self):
        """return a browser instance implemented by subclass"""
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
    # config chrome options
    arguments = settings.CHROME_ARGUMENTS
    # run chrome on mobile devices
    experiment = settings.CHROME_EXPERIMENTAL
    # webdriver manager to manage latest match driver for chrome
    service = ChromeService(executable_path=ChromeDriverManager().install())

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
            chrome = self._browser(service=self.service, options=self.options)
        else:  # default option for browser
            chrome = self._browser(service=self.service)

        if self.method_mark:  # set actions after the browser started
            chrome.implicitly_wait(self.implicit_time)
            chrome.set_script_timeout(self.script_time_out)
            chrome.set_page_load_timeout(self.page_load_time)
            chrome.delete_all_cookies()
            chrome.maximize_window()
            # chrome.set_window_size(*self.windows_size)

        return chrome


if __name__ == '__main__':
    with ChromeBrowser().browser as _chrome:
        _chrome.get('http://www.amazon.ca')
        sleep(3)
