#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-11 6:32 a.m.
# Author: Ding
from time import sleep

import settings
from page.base_page import BasePage
from page.checkout_page_step_one import CheckoutStepOnePage
from util.file_reader import YamlReader


class CartPage(BasePage):
    locators = YamlReader(settings.ELEMENT_LOCATOR['cart']).data

    def checkout(self):
        self.scroll_to_element(self.checkout_btn)
        sleep(2)
        self.click(self.checkout_btn)
        return CheckoutStepOnePage(self.driver)