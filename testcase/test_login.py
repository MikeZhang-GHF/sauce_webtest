#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-10 3:52 p.m.
# Author: Ding
from time import sleep

import allure
import pytest

import settings
from page.login_page import LoginPage
from util.file_reader import YamlReader
from util.report_util import add_img_to_report

# login test cases
login_data = YamlReader(settings.TEST_DATA['login']).data
# pass logins cases
data_pass = login_data['pass_logins']
# failed logins cases
data_fail = login_data['failed_logins']


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
