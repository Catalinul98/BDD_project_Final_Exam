Feature: Homepage Search Functionality

  Background:
    Given I am on the home page

  @search @smoke
  Scenario: Successful product search
    When I type "backpack" into the search bar
    And I press the search button
    Then I should be taken to the search results page showing items related to "backpack"

  @search @regression
  Scenario: Search for a non-existent product
    When I type "product1234" into the search bar
    And I press the search button
    Then I should be redirected to the catalog search product with no products displayed

  @search @smoke
  Scenario: Sort search results by price
    When I type "backpack" into the search bar
    And I press the search button
    Then I should be taken to the search results page showing items related to "backpack"
    When I select "Price" from the sort options
    Then I should see the products sorted from high to low prices on the page
    When I click on the button to set the order to ascending
    Then I should see the products sorted from low to high prices on the page

  @search @regression
  Scenario: Add two products to compare list
    When I click on the product "Radiant Tee"
    And I am redirected to the product details page
    And I click the "Add to Compare" button
    When I click on the product "Diva Gym Tee"
    And I am redirected to the product details page
    And I click the "Add to Compare" button
    When I click on the "Compare Products" button
    Then I should be taken to the compare products page
