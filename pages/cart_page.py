from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    HOME_PAGE_URL = "https://magento.softwaretestingboard.com/"
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[title='Add to Cart']")
    CART_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.message-success.success.message")
    SHOPPING_CART_LINK_TEXT = (By.LINK_TEXT, "shopping cart")
    REMOVE_ITEM_BUTTON = (By.CSS_SELECTOR, "a.action.action-delete")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "div.cart-empty")
    SIZE_OPTION = (By.ID, "option-label-size-143-item-168")
    COLOR_OPTION = (By.ID, "option-label-color-93-item-53")
    PRODUCT_FUSION_BACKPACK = (By.LINK_TEXT, "Fusion Backpack")
    PRODUCT_HERO_HOODIE = (By.LINK_TEXT, "Hero Hoodie")

    def navigate_to_home_page(self):
        """Navigates to the home page."""
        self.driver.get(self.HOME_PAGE_URL)

    def click_on_fusion_backpack(self):
        """Clicks on the 'Fusion Backpack' product link to go to its details page."""
        self.find(self.PRODUCT_FUSION_BACKPACK).click()

    def click_on_hero_hoodie(self):
        """Clicks on the 'Hero Hoodie' product link to go to its details page."""
        self.find(self.PRODUCT_HERO_HOODIE).click()

    def click_add_to_cart(self):
        """Clicks the 'Add to Cart' button on the product details page."""
        self.find(self.ADD_TO_CART_BUTTON).click()

    def verify_success_message(self, expected_message):
        """Verifies that the success message for adding an item to the cart is displayed.
        Raises an AssertionError if the expected message is not present."""
        success_message = self.get_text(self.CART_SUCCESS_MESSAGE)
        assert expected_message in success_message, f"Expected '{expected_message}', but got '{success_message}'"

    def navigate_to_shopping_cart_from_message(self):
        """Navigates to the shopping cart page via the hyperlink in the success message."""
        self.find(self.SHOPPING_CART_LINK_TEXT).click()

    def remove_item_from_cart(self):
        """Clicks on the 'Remove Item' button in the shopping cart to remove the item."""
        self.find(self.REMOVE_ITEM_BUTTON).click()

    def verify_empty_cart_message(self, expected_message):
        """Verifies that the message indicating the shopping cart is empty is displayed."""
        empty_message = self.get_text(self.EMPTY_CART_MESSAGE)
        assert expected_message in empty_message, f"Expected '{expected_message}', but got '{empty_message}'"

    def is_redirected_to_item_page(self):
        """Verifies that the browser is redirected to the item page by checking for the 'Add to Cart' button."""
        assert self.is_element_present(self.ADD_TO_CART_BUTTON), "Not redirected to the item page"

    def is_redirected_to_cart_page(self):
        """Verifies that the browser is redirected to the shopping cart page by checking for the 'Remove Item' button."""
        assert self.is_element_present(self.REMOVE_ITEM_BUTTON), "Not redirected to the shopping cart page"

    def select_size(self):
        """Selects the product size."""
        self.click(self.SIZE_OPTION)

    def select_color(self):
        """Selects the product color."""
        self.click(self.COLOR_OPTION)

