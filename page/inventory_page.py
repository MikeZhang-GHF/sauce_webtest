#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-10 7:56 p.m.
# Author: Ding
from time import sleep

import settings
from elementlocator.page_inventory import InventoryBase
from page.base_page import BasePage
from page.cart_page import CartPage
from util.file_reader import YamlReader


class InventoryPage(BasePage, InventoryBase):
    """
        Use the different locator encapsulation method
        The reason is:
            Inventory page is composed of many product components,
            the locating strategy is the same except the product name different.
            In order to reuse the locator code, we encapsulate the strategy within
            the locator method with product name as an input parameter.
            If the page have hundreds of product, yaml configure locating method
            could be very hard to be maintained because we have to write (k,v) for each
            product.
    """
    locators = YamlReader(settings.ELEMENT_LOCATOR['inventory']).data

    @property
    def avatar_text(self):
        return self.text(self.avatar)

    def add_to_cart(self, product_name):
        """use the different method to locate the product component add to cart button"""
        # add to cart only if the product is not in the cart
        _btn = self.add_to_cart_button(product_name)
        if self.text(_btn) == 'ADD TO CART':
            self.click(_btn)

    def goto_cart(self):
        self.scroll_to_element(self.cart_icon)
        sleep(1)
        self.click(self.cart_icon)
        return CartPage(self.driver)
