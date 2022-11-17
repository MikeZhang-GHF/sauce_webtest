#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-10 3:10 p.m.
# Author: Ding
# import os

"""
  for local test, the test report directory is report
  And the report directory can be changed by change -o your directory

  **go to settings.py to change HEADLESS for different browser to False**
  in order to visualize the automation test process on different browser
  The automation test run headless browser on server end.
"""
import os

if __name__ == '__main__':
    # cross browser test
    os.system("pytest -vs -n auto --alluredir=report --browser=chrome")
    # os.system("pytest -vs -n auto --browser=firefox")
    # os.system("pytest -vs -n auto --browser=edge")
    os.system(f"allure generate report{os.sep} -o report{os.sep}html --clean")
