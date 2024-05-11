from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage

class SearchPage(BasePage):
    INPUT_SEARCH = (By.ID, "search")
    BUTTON_SEARCH = (By.CSS_SELECTOR, "button.action.search")
    PRODUCTS_CONTAINER = (By.CSS_SELECTOR, "div.products-grid")
    SEARCH_RESULTS = (By.CSS_SELECTOR, "div.product-item-info")
    SORT_DROPDOWN = (By.CSS_SELECTOR, "select.sorter-options")

    def navigate_to_home_page(self):
        self.driver.get("https://magento.softwaretestingboard.com/")

    def set_search_term(self, text):
        input_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.INPUT_SEARCH)
        )
        input_element.clear()
        input_element.send_keys(text)

    def click_search_button(self):
        button_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BUTTON_SEARCH)
        )
        button_element.click()

    def verify_search_results_page(self, item):
        results = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.SEARCH_RESULTS)
        )
        return any(item.lower() in result.text.lower() for result in results)

    def select_sort_option(self, option_text):
        sort_dropdown = Select(WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SORT_DROPDOWN)
        ))
        sort_dropdown.select_by_visible_text(option_text)

    def verify_no_products_displayed(self):
        try:
            self.driver.find_element(*self.PRODUCTS_CONTAINER)
            return False
        except NoSuchElementException:
            return True

    def get_current_url(self):
        return self.driver.current_url
