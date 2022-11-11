#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-11 7:44 a.m.
# Author: Ding
from time import sleep

import allure
import pytest

import settings
from testdata.data_generator import DataGenerator
from util.file_reader import YamlReader
from util.report_util import add_img_to_report

# username, password = 'performance_glitch_user', 'secret_sauce'
# username, password = 'standard_user', 'secret_sauce'

two_products = ['Sauce Labs Bolt T-Shirt', 'Sauce Labs Onesie']
config_list = YamlReader(settings.TEST_DATA['purchase']).data

firstname = DataGenerator.firstname()
lastname = DataGenerator.lastname()
postalcode = DataGenerator.postalcode()


@allure.epic("Test Product Purchase Process")
@allure.story("Test designated product and configurable product list purchase process")
class TestPurchase:
    @pytest.mark.purchase
    @allure.feature("Test add two designated product purchase process")
    def test_purchase_two_products(self, login_fixture):
        self.__purchase_process(login_fixture, two_products)

    # @pytest.mark.purchase
    @allure.feature("Test configurable product list purchase process")
    def test_purchase_from_config_list(self, login_fixture):
        self.__purchase_process(login_fixture, config_list)

    def __purchase_process(self, login_fixture, product_list):
        inventory_page = login_fixture
        # get the driver
        _driver = inventory_page.driver

        with allure.step("Step 1: add product to the shopping cart"):
            for product in product_list:
                inventory_page.add_to_cart(product)
            # sleep(2)
            add_img_to_report(_driver, "add products to the shopping cart")

        with allure.step("Step 2: go to the shopping cart"):
            cart_page = inventory_page.goto_cart()
            add_img_to_report(_driver, "go to the shopping cart")

        with allure.step("Step 3: checkout"):
            checkout_step_one_page = cart_page.checkout()
            add_img_to_report(_driver, "checkout")

        with allure.step("Step 4: checkout: input your information"):
            checkout_step_one_page.input_info(firstname, lastname, postalcode)
            add_img_to_report(_driver, "checkout_step_one")

        with allure.step("Step 5: checkout: overview"):
            checkout_step_two_page = checkout_step_one_page.continue_checkout()
            add_img_to_report(_driver, "checkout_step_two")

        with allure.step("Step 6: checkout complete and assert"):
            checkout_complete_page = checkout_step_two_page.checkout_finish()
            add_img_to_report(_driver, "checkout_complete")
            assert 'CHECKOUT: COMPLETE!' in checkout_complete_page.checkout_complete_text
            sleep(1)

        with allure.step("Step 7: back to home"):
            checkout_complete_page.back_home()
            add_img_to_report(_driver, "back to home")
            sleep(1)
