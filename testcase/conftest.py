#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-10 3:47 p.m.
# Author: Ding
import pytest

from page.login_page import LoginPage
from util.browser import EdgeBrowser, FirefoxBrowser, ChromeBrowser

# valid login for login fixture
username, password = 'standard_user', 'secret_sauce'


@pytest.fixture(scope='session')
def driver(browser):
    """return different browser driver based on pytest option"""
    if browser == 'firefox':
        _driver = FirefoxBrowser().browser
    elif browser == 'edge':
        _driver = EdgeBrowser().browser
    else:
        _driver = ChromeBrowser().browser

    yield _driver
    _driver.quit()


def pytest_addoption(parser):
    """parse my addoption for pytest"""
    parser.addoption(
        "--browser",
        default="chrome",
        help="cross browser option: chrome, firefox, or edge"
    )


@pytest.fixture(scope='session')
def browser(request):
    """get the browser argument"""
    return request.config.getoption('--browser')


@pytest.fixture()
def login_fixture(driver):
    """login fixture setup for testcase"""
    return LoginPage(driver).login_pass(username, password)
