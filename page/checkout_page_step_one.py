#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-11 6:48 a.m.
# Author: Ding

import settings
from page.base_page import BasePage
from page.checkout_page_step_two import CheckoutStepTwoPage
from util.file_reader import YamlReader


class CheckoutStepOnePage(BasePage):
    locators = YamlReader(settings.ELEMENT_LOCATOR['checkout_one']).data

    def input_info(self, firstname, lastname, postalcode):
        self.send_keys(self.firstname, firstname)
        self.send_keys(self.lastname, lastname)
        self.send_keys(self.postalcode, postalcode)

    def continue_checkout(self):
        self.scroll_to_continue_button()
        self.click(self.continue_btn)
        return CheckoutStepTwoPage(self.driver)

    def scroll_to_continue_button(self):
        """for the better screenshot"""
        self.scroll_to_element(self.continue_btn)
