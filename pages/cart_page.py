from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):

    # Selectors
    PRODUCT_LINK = (By.LINK_TEXT, "Fusion Backpack")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[title='Add to Cart']")
    CART_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.message-success.success.message")
    SHOPPING_CART_LINK_TEXT = (By.LINK_TEXT, "shopping cart")
    REMOVE_ITEM_BUTTON = (By.CSS_SELECTOR, "a.action.action-delete")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "div.cart-empty")

    def navigate_to_home_page(self):
        """Navigates to the home page."""
        self.driver.get("https://magento.softwaretestingboard.com/")

    def click_on_product(self):
        """Clicks on the specified product link to go to its details page."""
        self.find(self.PRODUCT_LINK).click()

    def click_add_to_cart(self):
        """Clicks the 'Add to Cart' button on the product details page."""
        self.find(self.ADD_TO_CART_BUTTON).click()

    def verify_success_message(self):
        """Verifies that the success message for adding an item to the cart is displayed."""
        return self.get_text(self.CART_SUCCESS_MESSAGE)

    def navigate_to_shopping_cart_from_message(self):
        """Navigates to the shopping cart page via the hyperlink in the success message."""
        self.find(self.SHOPPING_CART_LINK_TEXT).click()

    def remove_item_from_cart(self):
        """Clicks on the 'Remove Item' button in the shopping cart to remove the item."""
        self.find(self.REMOVE_ITEM_BUTTON).click()

    def verify_empty_cart_message(self):
        """Verifies that the message indicating the shopping cart is empty is displayed."""
        return self.get_text(self.EMPTY_CART_MESSAGE)

    def is_redirected_to_item_page(self):
        """Verifies that the browser is redirected to the item page by checking for the 'Add to Cart' button."""
        return self.is_element_present(self.ADD_TO_CART_BUTTON)

    def is_redirected_to_cart_page(self):
        """Verifies that the browser is redirected to the shopping cart page by checking for the 'Remove Item' button."""
        return self.is_element_present(self.REMOVE_ITEM_BUTTON)
