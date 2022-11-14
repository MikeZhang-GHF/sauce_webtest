from time import sleep

import allure
import parse
from behave import given, when, then, register_type

from page.inventory_page import InventoryPage
from page.login_page import LoginPage
from util.report_util import add_img_to_report


@parse.with_pattern(r'.*')
def parse_nullable_string(text):
    return text


# allow empty input string from Scenario Outline
register_type(NullableString=parse_nullable_string)


@allure.epic("Test Login")
@given(u'I open chrome browser')
def open_browser(context):  # context must stay otherwise buggy
    print(context.driver)
    assert True


@when(u'I go to the website https://www.saucedemo.com/')
def goto_homepage(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.get()


@when(u'input username "{username:NullableString}" and password "{password:NullableString}"')
def input_username_password(context, username, password):
    context.login_page.input_username(username)
    context.login_page.input_password(password)
    context.username, context.password = username, password
    add_img_to_report(context.driver, "input username and password", need_sleep=False)
    sleep(1)


@when(u'click login button')
def click_login_button(context):
    context.login_page.click_login_button()
    context.inventory_page = InventoryPage(context.driver)


@allure.story("Test pass logins")
@allure.feature("Pass Logins")
@allure.description("Test pass logins")
@then(u'I should login and the page will include "Products"')
def pass_login(context):
    add_img_to_report(context.driver, "pass login to inventory page")
    assert 'PRODUCTS' in context.inventory_page.avatar_text
    sleep(1)


@allure.story("Test failed logins")
@allure.feature("Failed Logins")
@allure.description("Test failed logins")
@then(u'I should not login and the page will include "{expect_error}"')
def failed_login(context, expect_error):
    add_img_to_report(context.driver, "failed login error message")
    assert expect_error == context.login_page.error_message
    sleep(1)


# login background for other process
valid_username, valid_password = 'standard_user', 'secret_sauce'


@given(u'I login as a valid user')
def login_as_valid_user(context):
    context.login_page = LoginPage(context.driver)
    context.inventory_page = context.login_page.login_pass(valid_username, valid_password)
