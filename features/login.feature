Feature: Login Page

  Background: Open login page
    Given I am on the login page

  @regression @sanity
  Scenario: Check that the URL is correct
    Then The URL of the page is "https://magento.softwaretestingboard.com/customer/account/login"

  @regression @smoke
  Scenario Outline: Log in with unregistered email
    When I enter "<email>" in the email input
    And I enter "<password>" in the password input
    And I click the login button
    Then I should see "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later." message
    Examples:
      | email                | password         |
      | notuser@example.com  | 123456           |
      | fakeaccount@fake.com | password123      |
      | tryme@notreal.com    | incorrectpass    |
