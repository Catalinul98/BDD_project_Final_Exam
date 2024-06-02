from behave import when, then, given

@given('I start on the home page')
def step_impl(context):
    context.search_page.navigate_to_home_page()

@when('I type "{search_term}" into the search bar')
def step_impl(context, search_term):
    context.search_page.set_search_term(search_term)

@when('I press the search button')
def step_impl(context):
    context.search_page.click_search_button()

@then('I should be taken to the search results page showing items related to "{item}"')
def step_impl(context, item):
    context.search_page.verify_search_results_page(item)

@then('I should be redirected to the catalog search product with no products displayed')
def step_impl(context):
    context.search_page.verify_no_products_displayed()

@when('I select "Price" from the sort options')
def step_impl(context):
    context.search_page.select_sort_option()

@then('I should see the products sorted from high to low prices on the page')
def step_impl(context):
    context.search_page.verify_products_sorted_high_to_low()

@when('I click on the button to set the order to ascending')
def step_impl(context):
    context.search_page.click_sort_direction_button()

@then('I should see the products sorted from low to high prices on the page')
def step_impl(context):
    context.search_page.verify_products_sorted_low_to_high()

@when('I click on the product "{product_name}"')
def step_impl(context, product_name):
    context.search_page.click_on_product(product_name)

@when('I am redirected to the product details page')
def step_impl(context):
    context.search_page.verify_product_page()

@when('I click the "Add to Compare" button')
def step_impl(context):
    context.search_page.click_add_to_compare_button()

@when('I click on the "Compare Products" button')
def step_impl(context):
    context.search_page.click_compare_products_button()

@then('I should be taken to the compare products page')
def step_impl(context):
    context.search_page.verify_compare_products_page()

@when('I click on "Category"')
def step_impl(context):
    context.search_page.click_category_filter()

@when('I select "Gear" from the category filter')
def step_impl(context):
    context.search_page.select_gear_category()

@then('I should see only products from the "Gear" category')
def step_impl(context):
    context.search_page.verify_search_results_page()

@when('I navigate to the second page of results')
def step_impl(context):
    context.search_page.navigate_to_page_2()

@then('I should see the products from the second page')
def step_impl(context):
    context.search_page.verify_current_page(2)
