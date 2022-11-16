#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-10 3:47 p.m.
# Author: Ding
import pytest

from page.login_page import LoginPage
from util.browser import ChromeBrowser
from util.browser import EdgeBrowser
from util.browser import FirefoxBrowser

# get_driver = None

# valid login for login fixture
username, password = 'standard_user', 'secret_sauce'


@pytest.fixture(scope='session')
# @pytest.fixture()  # parallel testing
def driver():
    # _driver = ChromeBrowser().browser
    _driver = FirefoxBrowser().browser

    return _driver
    # if browser == 'firefox':
    #     _driver = FirefoxBrowser().browser
    # elif browser == 'edge':
    #     _driver = EdgeBrowser().browser
    # else:
    #     _driver = ChromeBrowser().browser
    #
    # yield _driver
    # _driver.quit()


# def pytest_add_option(parser):
#     parser.addoption('--browser')
#
#
# @pytest.fixture(scope='class', autouse=True)
# def browser(request):
#     return request.config.getoption('--browser')
#
#
@pytest.fixture()
def login_fixture(driver):
    return LoginPage(driver).login_pass(username, password)
