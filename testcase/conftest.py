#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-10 3:47 p.m.
# Author: Ding
import pytest

from util.browser import ChromeBrowser

global get_driver


@pytest.fixture()
def driver():
    global get_driver
    get_driver = ChromeBrowser().browser
    yield get_driver
    get_driver.quit()
