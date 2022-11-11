#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-11 6:49 a.m.
# Author: Ding
from time import sleep

import settings
from page.base_page import BasePage
from page.checkout_page_complete import CheckoutCompletePage
from util.file_reader import YamlReader


class CheckoutStepTwoPage(BasePage):
    locators = YamlReader(settings.ELEMENT_LOCATOR['checkout_two']).data

    def checkout_finish(self):
        self.scroll_to_element(self.finish_btn)
        sleep(1)
        self.click(self.finish_btn)
        sleep(1)
        return CheckoutCompletePage(self.driver)
