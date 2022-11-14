from behave import when, then

from testdata.data_generator import DataGenerator
from util.report_util import add_img_to_report

# fake data for checkout information
firstname = DataGenerator.firstname()
lastname = DataGenerator.lastname()
zipcode = DataGenerator.postalcode()


@when(u'click the checkout button to checkout step one page')
def click_checkout_button_to_checkout_step_one_page(context):
    context.cart_page.scroll_to_checkout_button()
    add_img_to_report(context.driver, "Go to checkout step one page")
    context.checkout_step_one_page = context.cart_page.checkout()


@when(u'input firstname, lastname, and zipcode')
def input_checkout_info(context):
    context.checkout_step_one_page.input_info(firstname, lastname, zipcode)
    add_img_to_report(context.driver, "Input check out info")


@when(u'click continue button to checkout step two page')
def click_continue_button_to_checkout_step_two_page(context):
    context.checkout_step_one_page.scroll_to_continue_button()
    add_img_to_report(context.driver, "Go to checkout step two page")
    context.checkout_step_two_page = context.checkout_step_one_page.continue_checkout()


@when(u'click finish button to checkout complete page')
def click_continue_button_to_checkout_complete_page(context):
    context.checkout_step_two_page.scroll_to_finish_button()
    add_img_to_report(context.driver, "Go to checkout step two page", need_sleep=False)
    context.checkout_complete_page = context.checkout_step_two_page.checkout_finish()


@then(u'I should go to the checkout complete page and see the checkout complete')
def checkout_complete(context):
    assert 'COMPLETE' in context.checkout_complete_page.checkout_complete_text
    add_img_to_report(context.driver, "Go to checkout complete page")
