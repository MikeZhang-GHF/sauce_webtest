#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-11 1:13 p.m.
# Author: Ding
from time import sleep

import allure


def add_img_to_report(driver, step_name, need_sleep=True):
    """add screenshot tot allure report"""
    if need_sleep:
        sleep(1)
    allure.attach(
        driver.get_screenshot_as_png(),
        f"{step_name}.png",
        allure.attachment_type.PNG
    )


