#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-11 6:07 a.m.
# Author: Ding
from time import sleep

import pytest


class TestInventoryPage:
    @pytest.mark.inventory
    @pytest.mark.skip("already included in purchase test")
    def test_add_to_cart(self, driver, login_fixture):
        products = [
            # 'Sauce Labs Backpack',
            'Sauce Labs Bolt T-Shirt',
            'Sauce Labs Onesie',
            # 'Sauce Labs Bike Light',
            # 'Sauce Labs Fleece Jacket',
            # 'Test.allTheThings() T-Shirt (Red)'
        ]
        inventory_page = login_fixture
        sleep(2)

        for product in products:
            inventory_page.add_to_cart(product)
        sleep(2)
