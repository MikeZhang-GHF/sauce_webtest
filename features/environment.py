#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-13 9:38 a.m.
# Author: Ding

from behave import fixture, use_fixture

from util.browser import ChromeBrowser


@fixture()
def chrome_driver(context):
    context.driver = ChromeBrowser().browser
    yield context.driver
    context.driver.quit()


def before_all(context):
    use_fixture(chrome_driver, context)
