from behave import given, when, then
import time

@given('I am on the register page')
def step_impl(context):
    context.register_page.open()

@given('I generate a unique email')
def step_impl(context):
    context.unique_email = f"user_{int(time.time())}@example.com"

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
    assert context.register_page.is_success_message_displayed(), "Success message was not displayed"

@then('The success message is "Thank you for registering with Main Website Store."')
def step_impl(context):
    success_text = context.register_page.get_success_message_text()
    assert success_text == "Thank you for registering with Main Website Store.", f"Expected success message not found. Found: {success_text}"

@then('The URL of the register page is "https://magento.softwaretestingboard.com/customer/account/create/"')
def step_impl(context):
    assert context.register_page.driver.current_url == "https://magento.softwaretestingboard.com/customer/account/create/", "URL is not correct"