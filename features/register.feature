Feature: Registration page

  Background: Open register page
    Given I am on the register page
    And I generate a unique email

  @regression @sanity
  Scenario: Check that the URL is correct
    Then The URL of the register page is "https://magento.softwaretestingboard.com/customer/account/create/"

  @regression @smoke
  Scenario: Register new account with valid data
    When I enter "TestFirstName" in the first name input
    And I enter "TestLastName" in the last name input
    And I enter the unique email in the email input
    And I enter "Password123" in the new password input
    And I enter "Password123" in the password confirm input
    And I click the create account button
    Then Success message is displayed
    And The success message is "Thank you for registering with Main Website Store."