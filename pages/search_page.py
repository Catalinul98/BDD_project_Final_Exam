from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage

class SearchPage(BasePage):
    INPUT_SEARCH = (By.ID, "search")
    BUTTON_SEARCH = (By.CSS_SELECTOR, "button.action.search")
    PRODUCTS_CONTAINER = (By.CSS_SELECTOR, "div.products-grid")
    SEARCH_RESULTS = (By.CSS_SELECTOR, "li.product-item")
    SORT_DROPDOWN = (By.CSS_SELECTOR, "select.sorter-options")
    SORT_DIRECTION_BUTTON = (By.CSS_SELECTOR, "a.action.sorter-action.sort-desc")
    SORTED_PRICES = (By.CSS_SELECTOR, "span.price")
    ADD_TO_COMPARE_BUTTON = (By.CSS_SELECTOR, "a.action.tocompare")
    COMPARE_PRODUCTS_BUTTON = (By.CSS_SELECTOR, "a.action.compare")
    COMPARE_PRODUCTS_TITLE = (By.CSS_SELECTOR, "div.page-title-wrapper span.base")  # Updated selector

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
        assert results, "No search results found on the page"
        for result in results:
            if item.lower() in result.text.lower():
                return True
        assert False, f"No results related to {item} found"

    def select_sort_option(self, option_text):
        sort_dropdown = Select(WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SORT_DROPDOWN)
        ))
        sort_dropdown.select_by_visible_text(option_text)

    def verify_no_products_displayed(self):
        try:
            self.driver.find_element(*self.PRODUCTS_CONTAINER)
            assert False, "Products were displayed when none were expected"
        except NoSuchElementException:
            pass

    def get_current_url(self):
        return self.driver.current_url

    def click_sort_direction_button(self):
        button_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SORT_DIRECTION_BUTTON)
        )
        button_element.click()

    def verify_products_sorted_high_to_low(self):
        prices = [float(price.text.replace('$', '').replace(',', '')) for price in self.driver.find_elements(*self.SORTED_PRICES) if price.text]
        assert prices == sorted(prices, reverse=True), "Products are not sorted from high to low prices"

    def verify_products_sorted_low_to_high(self):
        prices = [float(price.text.replace('$', '').replace(',', '')) for price in self.driver.find_elements(*self.SORTED_PRICES) if price.text]
        assert prices == sorted(prices), "Products are not sorted from low to high prices"

    def click_on_product(self, product_name):
        product_link = (By.LINK_TEXT, product_name)
        self.find(product_link).click()

    def verify_product_page(self):
        assert self.is_element_present(self.ADD_TO_COMPARE_BUTTON), "Not redirected to the product page"

    def click_add_to_compare_button(self):
        self.find(self.ADD_TO_COMPARE_BUTTON).click()

    def click_compare_products_button(self):
        self.find(self.COMPARE_PRODUCTS_BUTTON).click()

    def verify_compare_products_page(self):
        assert self.is_element_present(self.COMPARE_PRODUCTS_TITLE), "Not redirected to the compare products page"
