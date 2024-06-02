from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage


class SearchPage(BasePage):
    SORT_BY_PRICE = "Price"
    INPUT_SEARCH = (By.ID, "search")
    BUTTON_SEARCH = (By.CSS_SELECTOR, "button.action.search")
    PRODUCTS_CONTAINER = (By.CSS_SELECTOR, "div.products-grid")
    SEARCH_RESULTS = (By.CSS_SELECTOR, "li.product-item")
    SORT_DROPDOWN = (By.CSS_SELECTOR, "select.sorter-options")
    SORT_DIRECTION_BUTTON = (By.CSS_SELECTOR, "a.action.sorter-action.sort-desc")
    SORTED_PRICES = (By.CSS_SELECTOR, "span.price")
    ADD_TO_COMPARE_BUTTON = (By.CSS_SELECTOR, "a.action.tocompare")
    COMPARE_PRODUCTS_BUTTON = (By.CSS_SELECTOR, "a.action.compare")
    COMPARE_PRODUCTS_TITLE = (By.CSS_SELECTOR, "div.page-title-wrapper span.base")
    CATEGORY_FILTER = (By.CSS_SELECTOR, "#narrow-by-list > div > div.filter-options-title")
    GEAR_CATEGORY = (By.CSS_SELECTOR, "#narrow-by-list > div > div.filter-options-content > ol > li > a")
    PAGE_2 = (By.CSS_SELECTOR,
              "#maincontent > div.columns > div.column.main > div.search.results > div:nth-child(4) > div.pages > ul > li:nth-child(2) > a")

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

    def verify_search_results_page(self, item=None):
        results = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.SEARCH_RESULTS)
        )
        assert results, "No search results found on the page"

        if item:
            title_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "span.base[data-ui-id='page-title-wrapper']"))
            )
            assert item.lower() in title_element.text.lower(), f"Search results page title does not contain '{item}'"

    def select_sort_option(self):
        sort_dropdown = Select(WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SORT_DROPDOWN)
        ))
        sort_dropdown.select_by_visible_text(self.SORT_BY_PRICE)

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
        prices = [float(price.text.replace('$', '').replace(',', '')) for price in
                  self.driver.find_elements(*self.SORTED_PRICES) if price.text]
        assert prices == sorted(prices, reverse=True), "Products are not sorted from high to low prices"

    def verify_products_sorted_low_to_high(self):
        prices = [float(price.text.replace('$', '').replace(',', '')) for price in
                  self.driver.find_elements(*self.SORTED_PRICES) if price.text]
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

    def click_category_filter(self):
        category_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CATEGORY_FILTER)
        )
        category_element.click()

    def select_gear_category(self):
        gear_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.GEAR_CATEGORY)
        )
        gear_element.click()

    def navigate_to_page_2(self):
        page_2_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PAGE_2)
        )
        page_2_element.click()

    def verify_current_page(self, page_number):
        current_url = self.get_current_url()
        assert f'p={page_number}' in current_url, f"Not navigated to the page {page_number} of results"
