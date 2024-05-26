from behave import given, when, then

@given('I am on the register page')
def step_impl(context):
    context.register_page.open()

@given('I generate a unique email')
def step_impl(context):
    context.unique_email = context.register_page.generate_unique_email()

@when('I enter "TestFirstName" in the first name input')
def step_impl(context):
    context.register_page.set_first_name("TestFirstName")

@when('I enter "TestLastName" in the last name input')
def step_impl(context):
    context.register_page.set_last_name("TestLastName")

@when('I enter the unique email in the email input')
def step_impl(context):
    context.register_page.set_email(context.unique_email)

@when('I enter "Password123" in the new password input')
def step_impl(context):
    context.register_page.set_password("Password123")

@when('I enter "Password123" in the password confirm input')
def step_impl(context):
    context.register_page.set_confirm_password("Password123")

@when('I click the create account button')
def step_impl(context):
    context.register_page.click_register_button()

@then('Success message is displayed')
def step_impl(context):
    context.register_page.verify_success_message()

@then('The success message is "{expected_message}"')
def step_impl(context, expected_message):
    context.register_page.verify_success_message(expected_message)

@then('The URL of the register page is correct')
def step_impl(context):
    context.register_page.verify_url()
