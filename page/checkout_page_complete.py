#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-11 6:49 a.m.
# Author: Ding
import settings
from page.base_page import BasePage
from util.file_reader import YamlReader


class CheckoutCompletePage(BasePage):
    locators = YamlReader(settings.ELEMENT_LOCATOR['checkout_complete']).data

    def back_home(self):
        self.click(self.back_home_btn)

    @property
    def checkout_complete_text(self):
        self.scroll_to_element(self.checkout_complete)
        return self.text(self.checkout_complete)
