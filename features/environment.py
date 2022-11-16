#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-13 9:38 a.m.
# Author: Ding

from behave import fixture, use_fixture

from util.browser import ChromeBrowser, FirefoxBrowser, EdgeBrowser, SafariBrowser


@fixture()
def chrome_driver(context):
    context.driver = ChromeBrowser().browser
    yield context.driver
    context.driver.quit()


@fixture()
def firefox_driver(context):
    context.driver = FirefoxBrowser().browser
    yield context.driver
    context.driver.quit()


@fixture()
def edge_driver(context):
    context.driver = EdgeBrowser().browser
    yield context.driver
    context.driver.quit()


@fixture()
def safari_driver(context):
    context.driver = SafariBrowser().browser
    yield context.driver
    context.driver.quit()


def before_all(context):
    use_fixture(chrome_driver, context)
    # use_fixture(firefox_driver, context)
    # use_fixture(edge_driver, context)
