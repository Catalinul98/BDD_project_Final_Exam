from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time  # Utilizat pentru a genera un timestamp

class RegisterPage(BasePage):
    REGISTER_PAGE_URL = "https://magento.softwaretestingboard.com/customer/account/create/"
    INPUT_FIRST_NAME = (By.ID, "firstname")
    INPUT_LAST_NAME = (By.ID, "lastname")
    INPUT_EMAIL = (By.ID, "email_address")
    INPUT_PASSWORD = (By.ID, "password")
    INPUT_CONFIRM_PASSWORD = (By.ID, "password-confirmation")
    BUTTON_REGISTER = (By.XPATH, "//button[@title='Create an Account']")
    REGISTER_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.message-success.success.message")
    ERROR_MESSAGE_GENERAL = (By.CSS_SELECTOR, "div.message-error.error.message")

    def open(self):
        """Navigate to the register page URL."""
        self.driver.get(self.REGISTER_PAGE_URL)

    def set_first_name(self, first_name):
        """Enter first name into the first name input field."""
        self.type(self.INPUT_FIRST_NAME, first_name)

    def set_last_name(self, last_name):
        """Enter last name into the last name input field."""
        self.type(self.INPUT_LAST_NAME, last_name)

    def set_email(self, email):
        """Enter email into the email input field."""
        self.type(self.INPUT_EMAIL, email)

    def set_password(self, password):
        """Enter password into the password input field."""
        self.type(self.INPUT_PASSWORD, password)

    def set_confirm_password(self, password):
        """Enter password into the confirm password input field."""
        self.type(self.INPUT_CONFIRM_PASSWORD, password)

    def click_register_button(self):
        """Click the register button to submit the form."""
        self.find(self.BUTTON_REGISTER).click()

    def generate_unique_email(self):
        """Generate a unique email address."""
        timestamp = int(time.time())
        self.unique_email = f"test_{timestamp}@example.com"
        self.set_email(self.unique_email)
        return self.unique_email

    def verify_success_message(self, expected_message=None):
        """Verify that the registration success message is displayed and contains the expected text."""
        assert self.is_element_present(self.REGISTER_SUCCESS_MESSAGE), "Success message was not displayed"
        success_text = self.get_text(self.REGISTER_SUCCESS_MESSAGE)
        messages = [expected_message] if expected_message else ["Thank you for registering with Main Website Store."]
        for message in messages:
            if message not in success_text:
                raise AssertionError(f"Expected '{message}', but got '{success_text}'")

    def verify_url(self, expected_url=None):
        """Verify that the URL of the register page is correct."""
        expected_url = expected_url or self.REGISTER_PAGE_URL
        if self.driver.current_url != expected_url:
            raise AssertionError(f"URL is not correct. Expected {expected_url} but got {self.driver.current_url}")
