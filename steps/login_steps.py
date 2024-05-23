from behave import *

@given('I am on the login page')
def step_impl(context):
    context.login_page.open()

@then('The URL of the page is "{url}"')
def step_impl(context, url):
    context.login_page.verify_url(url)

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
    context.login_page.verify_main_error_message(expected_error)
