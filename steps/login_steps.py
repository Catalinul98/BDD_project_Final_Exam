from behave import *

@given('I am on the login page')
def step_impl(context):
    context.login_page.open()

@then('The URL of the page is "{url}"')
def step_impl(context, url):
    assert context.login_page.driver.current_url == url, "Login page URL is incorrect"

@when('I enter "{email}" in the email input')
def step_impl(context, email):
    context.login_page.set_email(email)

@when('I enter "{password}" in the password input')
def step_impl(context, password):
    context.login_page.set_password(password)

@when('I click the login button')
def step_impl(context):
    context.login_page.click_login_button()

@then('I should see "{expected_error}" message')
def step_impl(context, expected_error):
    assert context.login_page.is_main_error_message_displayed(), "Error message not displayed"
    assert context.login_page.main_error_message_contains_text(expected_error), f"Error message does not contain the expected text: {expected_error}"