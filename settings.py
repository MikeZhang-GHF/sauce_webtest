#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-10 3:10 p.m.
# Author: Ding

import logging
import os

# project base dir
BASE_DIR = os.path.dirname(__file__)

# ----------------Browser Driver Attributes-------------
# Base browser attributes
DRIVER_BASE_DIR = os.path.join(BASE_DIR, 'driver')

CHROME_DRIVER_PATH = os.path.join(DRIVER_BASE_DIR, "chrome_driver")
FIREFOX_DRIVER_PATH = os.path.join(DRIVER_BASE_DIR, "firefox_driver")
EDGE_DRIVER_PATH = os.path.join(DRIVER_BASE_DIR, "edge_driver")
IE_DRIVER_PATH = os.path.join(DRIVER_BASE_DIR, "ie_driver")

HEADLESS = False
IMPLICITLY_WAIT_TIME = 20
PAGE_LOAD_TIME = 20
SCRIPT_TIMEOUT = 20
WINDOW_SIZE = 1920, 1024

# ----------------Chrome属性--------------
# Chrome启动参数开关
CHROME_OPTION_MARK = True

# Chrome浏览器操作开关
CHROME_METHOD_MARK = True

# headless
CHROME_HEADLESS = False
# page load time
CHROME_PAGE_LOAD_TIME = 40
# javascript execution time out
CHROME_SCRIPT_TIMEOUT = 30
# window size
CHROME_WINDOW_SIZE = 1920, 1080

# webdriver experimental
CHROME_EXPERIMENTAL = {
    'excludeSwitches': ['enable-automation'],
    # 'mobileEmulation': {'deviceName': 'iPhone 6'},
}

# Chrome option params
CHROME_ARGUMENTS = [
    "--start-maximized",
    "--ignore-certificate-errors",
    "--allow-insecure-localhost",
    "--incognito",
    "--disable-gpu",
    "--no-sandbox",
    "--disable-dev-shm-usage",
]

# -------Web element operation-------
# web element location wait time
UI_TIME_OUT = 300
POLL_FREQUENCY = 0.5

# -------project urls-------------
# project 1
SAUCE_PROJECT = 'https://www.saucedemo.com/'

# module 1 path

# database ini file path
DATABASE_INI_PATH = os.path.join(BASE_DIR, 'database.ini')

# ------ test suite --------
# smoke test
SUITE_SMOKE = []
# function 1 test
SUITE_FUNCTION_1 = []
# main test suite
SUITE_PROJECT1 = []

# ---------Web Element Yaml file----------

# web element yaml file base path
ELEMENTS_LOCATOR_DIR = os.path.join(BASE_DIR, 'elementlocator')
# element locators on pages under test
ELEMENT_LOCATOR = {
    'login': os.path.join(ELEMENTS_LOCATOR_DIR, 'page_login.yml'),
    'inventory': os.path.join(ELEMENTS_LOCATOR_DIR, 'page_inventory.yml'),
    'cart': os.path.join(ELEMENTS_LOCATOR_DIR, 'page_cart.yml'),
    'checkout_one': os.path.join(ELEMENTS_LOCATOR_DIR, 'page_checkout_step_one.yml'),
    'checkout_two': os.path.join(ELEMENTS_LOCATOR_DIR, 'page_checkout_step_two.yml'),
    'checkout_complete': os.path.join(ELEMENTS_LOCATOR_DIR, 'page_checkout_complete.yml'),
}

# ---------Test Data Yaml file------------
# Test data file base path
TEST_DATA_FILE_DIR = os.path.join(BASE_DIR, 'testdata')
TEST_DATA = {
    'login': os.path.join(TEST_DATA_FILE_DIR, 'login_data.yml'),
    'purchase': os.path.join(TEST_DATA_FILE_DIR, 'purchase_data.yml')
}

# Image file base path
IMG_FILE_DIR = os.path.join(BASE_DIR, 'img')

# Screenshot base path
SCREENSHOT_DIR = os.path.join(BASE_DIR, 'screenshot')

# Web element screenshot path
SCREENSHOT_ELEMENT_DIR = os.path.join(SCREENSHOT_DIR, 'element')
# ---------Email-----------------
EMAIL_SENDER = 'zhixiang.zhang2011@gmail.com'
EMAIL_RECEIVER = 'zhixiang.zhang2011@gmail.com'
EMAIL_SUBJECT = 'python_test'
EMAIL_SERVER = 'smtp.gmail.com'
EMAIL_AUTH_CODE = 'gjaubifmuexirlmh'  # 'ktwrfqqeucrnmdrp'
EMAIL_MESSAGE = 'automation test result'
EMAIL_ATTACHMENT = None

# ----------log file--------------
LOG_FORMATTER = ('%(asctime)s - %(name)s - %(levelname)s - %(status)s - %(message)s',
                 '%H:%M:%S')
LOG_NAME = r'test_log'
LOG_FILE = os.path.join(BASE_DIR, 'logs')
LOG_LEVEL = logging.DEBUG
