#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-10 3:52 p.m.
# Author: Ding
from time import sleep

import allure
import pytest

from page.login_page import LoginPage
from util.report_util import add_img_to_report

# login pass test cases
data_pass = [
    ('standard_user', 'secret_sauce'),
    # ('problem_user', 'secret_sauce'),
    # ('performance_glitch_user', 'secret_sauce'),
]

# negative cases
data_fail = [
    # ('standard_user', '', 'Epic sadface: Password is required'),  # no password
    # no username
    # ('', '', 'Epic sadface: Username is required'),
    # wrong username
    # ('wrong_username', 'secret_sauce', 'Epic sadface: Username and password do not match any user in this service'),
    # wrong password
    # ('standard_user', 'wrong_password', 'Epic sadface: Username and password do not match any user in this service'),
    # lockout user
    ('locked_out_user', 'secret_sauce', 'Epic sadface: Sorry, this user has been locked out.'),

]


@allure.epic("Login Test")
@allure.story("Test pass and failed logins")
class TestLogin:
    @pytest.mark.login_pass
    @allure.feature("Pass Logins")
    @allure.description("Test pass logins")
    @pytest.mark.parametrize('username, password', data_pass)
    def test_login_pass(self, username, password, driver):
        with allure.step("Step 1: input username and password."):
            login_page = LoginPage(driver)

        with allure.step("Step 2: click login to the inventory page."):
            inventory_page = login_page.login_pass(username, password)
            assert 'PRODUCTS' in inventory_page.avatar_text
            sleep(2)
            add_img_to_report(driver, "pass_logins")

    @pytest.mark.login_fail
    @allure.feature("Failed Logins")
    @allure.description("Test failed logins")
    @pytest.mark.parametrize('username, password, expect', data_fail)
    def test_login_fail(self, username, password, expect, driver):
        with allure.step("Step 1: input username and password."):
            page = LoginPage(driver)

        with allure.step("Step 2: click login to the inventory page."):
            page.login_fail(username, password)
            assert page.error_message == expect
            sleep(2)
            add_img_to_report(driver, "failed_logins")
