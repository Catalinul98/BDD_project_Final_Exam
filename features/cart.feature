Feature: Shopping Cart Functionality

  Background: User navigates to the home page
    Given I am on the home page

  @regression @smoke
  Scenario: Add specific item to shopping cart and then remove it
    When I click on the product "Fusion Backpack"
    And I am redirected to the item page
    And I click the "Add to Cart" button
    Then the message "You added Fusion Backpack to your shopping cart." should appear on the page
    When I click on the "shopping cart" link from the success message
    And I am redirected to the shopping cart page
    And I click on the "Remove Item" button
    Then the message "You have no items in your shopping cart." should be displayed

  Scenario: Select product size and color, then add to shopping cart
    When I click on the product "Hero Hoodie"
    And I am redirected to the item page
    And I select the size "M"
    And I select the color "Green"
    And I click the "Add to Cart" button
    Then the message "You added Hero Hoodie to your shopping cart." should appear on the page
