#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-10 3:40 p.m.
# Author: Ding

import settings
from page.base_page import BasePage
from page.inventory_page import InventoryPage
from util.file_reader import YamlReader


class LoginPage(BasePage):
    locators = YamlReader(settings.ELEMENT_LOCATOR['login']).data

    def __login_process(self, username, password):
        # go to website
        self.get()
        # input username
        self.input_username(username)
        # input password
        self.input_password(password)
        # click login button
        self.click_login_button()

    def input_username(self, username):
        self.send_keys(self.username, username)

    def input_password(self, password):
        self.send_keys(self.password, password)

    def click_login_button(self):
        self.click(self.login_btn)

    def login_pass(self, username: str, password: str):
        self.__login_process(username, password)
        return InventoryPage(self.driver)

    def login_fail(self, username: str, password: str):
        self.__login_process(username, password)
        return self

    @property
    def error_message(self):
        return self.text(self.error_msg)
