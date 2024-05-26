from behave import given, when, then

@given('I am on the home page')
def step_impl(context):
    context.cart_page.navigate_to_home_page()

@when('I click on the product "Fusion Backpack"')
def step_impl(context):
    context.cart_page.click_on_fusion_backpack()

@when('I click on the product "Hero Hoodie"')
def step_impl(context):
    context.cart_page.click_on_hero_hoodie()

@when('I am redirected to the item page')
def step_impl(context):
    context.cart_page.is_redirected_to_item_page()

@when('I click the "Add to Cart" button')
def step_impl(context):
    context.cart_page.click_add_to_cart()

@then('the message "{expected_message}" should appear on the page')
def step_impl(context, expected_message):
    context.cart_page.verify_success_message(expected_message)

@when('I click on the "shopping cart" link from the success message')
def step_impl(context):
    context.cart_page.navigate_to_shopping_cart_from_message()

@when('I am redirected to the shopping cart page')
def step_impl(context):
    context.cart_page.is_redirected_to_cart_page()

@when('I click on the "Remove Item" button')
def step_impl(context):
    context.cart_page.remove_item_from_cart()

@then('the message "{expected_message}" should be displayed')
def step_impl(context, expected_message):
    context.cart_page.verify_empty_cart_message(expected_message)

@when('I select the size "M"')
def step_impl(context):
    context.cart_page.select_size()

@when('I select the color "Green"')
def step_impl(context):
    context.cart_page.select_color()
