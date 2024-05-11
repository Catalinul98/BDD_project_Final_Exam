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

    def is_main_error_message_displayed(self):
        """Check if the main error message is displayed on the page."""
        return self.find(self.ERROR_MESSAGE).is_displayed()

    def main_error_message_contains_text(self, text):
        """Check if the main error message contains specific text."""
        return text in self.get_text(self.ERROR_MESSAGE)