#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-10 3:47 p.m.
# Author: Ding
import pytest

from page.login_page import LoginPage
from util.browser import ChromeBrowser

get_driver = None

# valid login for login fixture
username, password = 'standard_user', 'secret_sauce'


@pytest.fixture(scope='session')
# @pytest.fixture()  # parallel testing
def driver():
    global get_driver
    get_driver = ChromeBrowser().browser
    yield get_driver
    get_driver.quit()


@pytest.fixture()
def login_fixture(driver):
    return LoginPage(driver).login_pass(username, password)
