import allure
from behave import given, when, then

from util.report_util import add_img_to_report


@allure.story("BDD-test purchase process")
@allure.feature("Add product to cart")
@allure.description("add product to cart")
@given(u'a list of products')
def product_list(context):
    context.product_list = []
    for row in context.table:
        context.product_list.append(row['product'])


@when(u'I add each product to the shopping cart')
def add_product_to_cart(context):
    for product in context.product_list:
        context.inventory_page.add_to_cart(product)
    add_img_to_report(context.driver, "Add product to cart", need_sleep=False)


@when(u'click the shopping cart icon to go to the cart page')
def click_cart_icon(context):
    context.cart_page = context.inventory_page.goto_cart()
    add_img_to_report(context.driver, "Go to cart page")


@then(u'I should go to the cart page and see the products are in the shopping cart')
def in_cart_page(context):
    assert context.cart_page.checkout_button_text == 'CHECKOUT'
