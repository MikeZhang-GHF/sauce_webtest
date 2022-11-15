from time import sleep
from typing import Type, Union

# import different browser and their options
from selenium.webdriver import Chrome, ChromeOptions, Firefox, FirefoxOptions, Edge, EdgeOptions, Safari
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

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
    # webdriver manager to manage matched driver for chrome
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


class FirefoxBrowser(Browser):
    # add option mark to use default options or customized options
    option_mark = settings.FIREFOX_OPTION_MARK
    # config the browser after it starts
    method_mark = settings.FIREFOX_METHOD_MARK

    # override base class Browser attribute
    headless = settings.FIREFOX_HEADLESS
    page_load_time = settings.FIREFOX_PAGE_LOAD_TIME
    script_time_out = settings.FIREFOX_SCRIPT_TIMEOUT

    service = FirefoxService(executable_path=GeckoDriverManager().install())

    def __init__(self):
        super().__init__(browser_type=Firefox, option_type=FirefoxOptions)

    @property
    def options(self):
        return self._option()

    @property
    def browser(self):
        if self.options:  # set options for browser before it starts
            firefox = self._browser(service=self.service, options=self.options)
        else:  # default option for browser
            firefox = self._browser(service=self.service)

        if self.method_mark:  # set actions after the browser started
            firefox.implicitly_wait(self.implicit_time)
            firefox.set_script_timeout(self.script_time_out)
            firefox.set_page_load_timeout(self.page_load_time)
            firefox.delete_all_cookies()
            firefox.maximize_window()

        return firefox


class EdgeBrowser(Browser):
    # add option mark to use default options or customized options
    option_mark = settings.EDGE_OPTION_MARK
    # config the browser after it starts
    method_mark = settings.EDGE_METHOD_MARK

    # override base class Browser attribute
    headless = settings.EDGE_HEADLESS
    page_load_time = settings.EDGE_PAGE_LOAD_TIME
    script_time_out = settings.EDGE_SCRIPT_TIMEOUT
    clean_session = settings.EDGE_CLEAN_SESSION

    service = EdgeService(executable_path=EdgeChromiumDriverManager().install())

    def __init__(self):
        super().__init__(browser_type=Edge, option_type=EdgeOptions)

    @property
    def options(self):
        return self._option()

    @property
    def browser(self):
        if self.options:  # set options for browser before it starts
            edge = self._browser(service=self.service, options=self.options)
        else:  # default option for browser
            edge = self._browser(service=self.service)

        if self.method_mark:  # set actions after the browser started
            edge.implicitly_wait(self.implicit_time)
            edge.set_script_timeout(self.script_time_out)
            edge.set_page_load_timeout(self.page_load_time)
            edge.delete_all_cookies()
            edge.maximize_window()

        return edge


class SafariBrowser:
    # add option mark to use default options or customized options
    option_mark = settings.SAFARI_OPTION_MARK
    # config the browser after it starts
    method_mark = settings.SAFARI_METHOD_MARK

    # override base class Browser attribute
    implicit_time = settings.SAFARI_IMPLICITLY_WAIT_TIME
    headless = settings.SAFARI_HEADLESS
    page_load_time = settings.SAFARI_PAGE_LOAD_TIME
    script_time_out = settings.SAFARI_SCRIPT_TIMEOUT
    # Safari has preinstalled webdriver
    service = None

    @property
    def options(self):
        return

    @property
    def browser(self):
        if self.options:  # set options for browser before it starts
            safari = Safari(service=self.service, options=self.options)
        else:  # default option for browser
            safari = Safari(service=self.service)

        if self.method_mark:  # set actions after the browser started
            safari.implicitly_wait(self.implicit_time)
            safari.set_script_timeout(self.script_time_out)
            safari.set_page_load_timeout(self.page_load_time)
            safari.delete_all_cookies()
            safari.maximize_window()

        return safari


if __name__ == '__main__':
    with FirefoxBrowser().browser as _firefox:
        _firefox.get('http://www.amazon.ca')
        sleep(3)
