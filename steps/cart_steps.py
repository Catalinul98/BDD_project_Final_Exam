from behave import given, when, then

@given('I am on the home page "https://magento.softwaretestingboard.com/"')
def step_impl(context):
    context.cart_page.navigate_to_home_page()

@when('I click on the product "Fusion Backpack"')
def step_impl(context):
    context.cart_page.click_on_product()

@when('I am redirected to the item page')
def step_impl(context):
    assert context.cart_page.is_redirected_to_item_page(), "Not redirected to the item page"

@when('I click the "Add to Cart" button')
def step_impl(context):
    context.cart_page.click_add_to_cart()

@then('the message "You added Fusion Backpack to your shopping cart." should appear on the page')
def step_impl(context):
    success_message = context.cart_page.verify_success_message()
    assert "You added Fusion Backpack to your shopping cart." in success_message, "Success message did not appear"

@when('I click on the "shopping cart" link from the success message')
def step_impl(context):
    context.cart_page.navigate_to_shopping_cart_from_message()

@when('I am redirected to the shopping cart page')
def step_impl(context):
    assert context.cart_page.is_redirected_to_cart_page(), "Not redirected to the shopping cart page"

@when('I click on the "Remove Item" button')
def step_impl(context):
    context.cart_page.remove_item_from_cart()

@then('the message "You have no items in your shopping cart." should be displayed')
def step_impl(context):
    empty_message = context.cart_page.verify_empty_cart_message()
    assert "You have no items in your shopping cart." in empty_message, "Empty cart message did not appear"