#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-11 6:07 a.m.
# Author: Ding
from time import sleep

from page.login_page import LoginPage


class TestInventoryPage:

    def test_add_to_cart(self, driver):
        inventory_page = LoginPage(driver).login_pass('locked_out_user', 'secret_sauce')
        products = [
            'Sauce Labs Backpack',
            'Sauce Labs Bolt T-Shirt',
            'Sauce Labs Onesie',
            'Sauce Labs Bike Light',
            'Sauce Labs Fleece Jacket',
            'Test.allTheThings() T-Shirt (Red)'
        ]

        for product in products:
            inventory_page.add_to_cart(product)
        sleep(2)
