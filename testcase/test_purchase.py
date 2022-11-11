#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-11 7:44 a.m.
# Author: Ding
from time import sleep

import settings
from page.login_page import LoginPage
from testdata.data_generator import DataGenerator
from util.file_reader import YamlReader

# username, password = 'performance_glitch_user', 'secret_sauce'
username, password = 'standard_user', 'secret_sauce'

two_products = ['Sauce Labs Bolt T-Shirt', 'Sauce Labs Onesie']
config_list = YamlReader(settings.TEST_DATA['purchase']).data

firstname = DataGenerator.firstname()
lastname = DataGenerator.lastname()
postalcode = DataGenerator.postalcode()


class TestPurchase:

    def test_purchase_two_products(self, driver):
        self.__purchase_process(driver, two_products)

    def test_purchase_from_config_list(self, driver):
        self.__purchase_process(driver, config_list)

    def __purchase_process(self, driver, product_list):
        inventory_page = LoginPage(driver).login_pass(username, password)

        for product in product_list:
            inventory_page.add_to_cart(product)

        cart_page = inventory_page.goto_cart()
        checkout_step_one_page = cart_page.checkout()
        checkout_step_one_page.input_info(firstname, lastname, postalcode)
        checkout_step_two_page = checkout_step_one_page.continue_checkout()
        checkout_complete_page = checkout_step_two_page.checkout_finish()
        assert 'CHECKOUT: COMPLETE!' in checkout_complete_page.checkout_complete_text
        sleep(1)
        checkout_complete_page.back_home()
        sleep(1)
