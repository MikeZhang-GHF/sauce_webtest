#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-13 1:33 p.m.
# Author: Ding
import os

if __name__ == '__main__':
    print("start behavior driven test....")
    # start behavior driven test
    os.system(
        "behave -f allure_behave.formatter:AllureFormatter "
        "-o bdd_test_report/ "
        "features/ --exclude inventory.feature")
    # generate test report by allure
    # os.system(
    #     "allure generate bdd_test_report/ "
    #     "-o bdd_test_report/html --clean")
    # print("finish behavior driven test!")
