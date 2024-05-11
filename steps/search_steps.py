from behave import given, when, then

@given('I am on the home page "{url}"')
def step_impl(context, url):
    context.search_page.navigate_to_home_page()

@when('I type "{search_term}" into the search bar')
def step_impl(context, search_term):
    context.search_page.set_search_term(search_term)

@when('I press the search button')
def step_impl(context):
    context.search_page.click_search_button()

@then('I should be taken to the search results page showing items related to "{item}"')
def step_impl(context, item):
    assert context.search_page.verify_search_results_page(item), f"Search results do not show items related to {item}"

@when('I select "{sort_option}" from the sort options')
def step_impl(context, sort_option):
    context.search_page.select_sort_option(sort_option)

@then('I should see the products sorted from high to low prices on the page')
def step_impl(context):
    pass

@when('I click on the button to set the order to ascending')
def step_impl(context):
    pass

@then('I should see the products sorted from low to high prices on the page')
def step_impl(context):
    pass

@then('I should be redirected to the catalog search product with no products displayed')
def step_impl(context):
    expected_url_part = "catalogsearch/result"
    current_url = context.search_page.get_current_url()
    assert expected_url_part in current_url, f"URL is not as expected for search results, got {current_url}"
    assert context.search_page.verify_no_products_displayed(), "Expected no products to be displayed, but some were found"
