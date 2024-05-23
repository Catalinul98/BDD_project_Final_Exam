from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    LOGIN_PAGE_URL = "https://magento.softwaretestingboard.com/customer/account/login"
    INPUT_EMAIL = (By.ID, "email")
    INPUT_PASSWORD = (By.ID, "pass")
    BUTTON_LOGIN = (By.ID, "send2")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.message-error.error.message")

    def open(self):
        """Navigate to the login page URL."""
        self.driver.get(self.LOGIN_PAGE_URL)

    def set_email(self, text):
        """Enter text into the email input field."""
        self.type(self.INPUT_EMAIL, text)

    def set_password(self, text):
        """Enter text into the password input field."""
        self.type(self.INPUT_PASSWORD, text)

    def click_login_button(self):
        """Click the login button to submit the credentials."""
        self.find(self.BUTTON_LOGIN).click()

    def verify_url(self, expected_url):
        """Verify that the URL of the page is correct."""
        assert self.driver.current_url == expected_url, "Login page URL is incorrect"

    def verify_main_error_message(self, expected_error):
        """Verify that the main error message is displayed and contains the expected text."""
        assert self.is_element_present(self.ERROR_MESSAGE), "Error message not displayed"
        actual_error = self.get_text(self.ERROR_MESSAGE)
        errors = [expected_error]
        for error in errors:
            assert error in actual_error, f"Error message does not contain the expected text: {error}"
