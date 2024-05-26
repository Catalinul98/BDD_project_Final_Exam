from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from browser import Browser

class BasePage(Browser):

    INPUT_SEARCH = (By.ID, "search")
    BUTTON_SEARCH = (By.CSS_SELECTOR, "button[title='Search']")

    # Common methods
    def find(self, locator):
        """Find an element on the page."""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def type(self, locator, text):
        """Type text into an input field."""
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Get text from a page element."""
        return self.find(locator).text

    def select_by_text(self, locator, text):
        """Select a dropdown menu option by visible text."""
        dropdown = Select(self.find(locator))
        dropdown.select_by_visible_text(text)

    def select_by_index(self, locator, index):
        """Select a dropdown menu option by index."""
        dropdown = Select(self.find(locator))
        dropdown.select_by_index(index)

    def is_url_correct(self, expected_url):
        """Check if the current URL matches the expected URL."""
        return self.driver.current_url == expected_url

    def is_element_present(self, locator):
        """Check if an element is present on the page."""
        try:
            self.find(locator)
            return True
        except NoSuchElementException:
            return False

    def click(self, locator):
        """Click on an element identified by locator."""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.find(locator).click()

    def wait_for_element(self, locator):
        """Wait for an element to be visible and return it."""
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def set_search_term(self, text):
        """Enter text into the search field."""
        self.type(self.INPUT_SEARCH, text)

    def click_search_button(self):
        """Click the search button."""
        self.find(self.BUTTON_SEARCH).click()

    def verify_elements_present(self, locators):
        """Check if multiple elements are present on the page."""
        for locator in locators:
            assert self.is_element_present(locator), f"Element {locator} not present"
