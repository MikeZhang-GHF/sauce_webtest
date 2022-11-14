#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-10 3:10 p.m.
# Author: Ding

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

# ----------------Chrome Option Config--------------
# Chrome config option switch
CHROME_OPTION_MARK = True

# Chrome operation switch
CHROME_METHOD_MARK = True

# headless
CHROME_HEADLESS = True
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

# -------Web Element Locating and Operation Config-------
# web element location wait time
UI_TIME_OUT = 300
POLL_FREQUENCY = 0.5

# -------project urls-------------
# project 1
SAUCE_PROJECT = 'https://www.saucedemo.com/'

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

# Screenshot base path
SCREENSHOT_DIR = os.path.join(BASE_DIR, 'screenshot')

# Web element screenshot path
SCREENSHOT_ELEMENT_DIR = os.path.join(SCREENSHOT_DIR, 'element')
