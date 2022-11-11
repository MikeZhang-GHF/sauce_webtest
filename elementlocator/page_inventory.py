#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-11 9:56 a.m.
# Author: Ding

class InventoryBase:

    @classmethod
    def add_to_cart_button(cls, product_name):
        return "xpath", f"//div[text()='{product_name}']" \
                        f"/ancestor::div[@class='inventory_item']" \
                        f"//button[text()='Add to cart']"


if __name__ == '__main__':
    print(InventoryBase.add_to_cart_button('Test.allTheThings() T-Shirt (Red)'))
