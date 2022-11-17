#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-13 1:33 p.m.
# Author: Ding

"""
  for local test, the test report directory is report
  And the report directory can be changed by change -o your directory

  **go to settings.py to change HEADLESS for different browser to False**
  in order to visualize the automation test process on different browser
  The automation test run headless browser on server end.
"""

import os

if __name__ == '__main__':
    print("start behavior driven test....")
    # start behavior driven test
    os.system(
        f"behave -f allure_behave.formatter:AllureFormatter "
        f"-o bdd_test_report{os.sep} "
        f"features{os.sep} --exclude inventory.feature")
    # generate test report by allure
    os.system(
        f"allure generate bdd_test_report{os.sep} "
        f"-o bdd_test_report{os.sep}html --clean")
    print("finish behavior driven test!")
