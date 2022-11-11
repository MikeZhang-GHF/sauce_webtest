#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-10 3:52 p.m.
# Author: Ding
from time import sleep

import pytest

from page.login_page import LoginPage

# login pass test cases
data_pass = [
    ('standard_user', 'secret_sauce'),
    ('problem_user', 'secret_sauce'),
    ('performance_glitch_user', 'secret_sauce'),
]

# negative cases
data_fail = [
    # ('standard_user', '', 'Epic sadface: Password is required'),  # no password
    # ('', '', 'Epic sadface: Username is required'),  # no username
    # wrong username
    # ('wrong_username', 'secret_sauce', 'Epic sadface: Username and password do not match any user in this service'),
    # wrong password
    # ('standard_user', 'wrong_password', 'Epic sadface: Username and password do not match any user in this service'),
    # lockout user
    ('locked_out_user', 'secret_sauce', 'Epic sadface: Sorry, this user has been locked out.'),

]


class TestLogin:

    @pytest.mark.parametrize('username, password', data_pass)
    def test_login_pass(self, username, password, driver):
        login_page = LoginPage(driver)
        inventory_page = login_page.login_pass(username, password)
        assert 'PRODUCTS' in inventory_page.avatar_text
        sleep(2)

    @pytest.mark.parametrize('username, password, expect', data_fail)
    def test_login_fail(self, username, password, expect, driver):
        page = LoginPage(driver)
        page.login_fail(username, password)
        assert page.error_message == expect
        sleep(2)
