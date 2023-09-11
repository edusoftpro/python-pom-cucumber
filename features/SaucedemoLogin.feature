Feature: Saucedemo Login

  Scenario: Successful Login
    Given I am on the login page
    When I enter a valid "standard_user"
    And I enter a "secret_sauce"
    When I click the login button
    Then I should see a shopping cart

  Scenario: Invalid Credentials
    Given I am on the login page
    When I enter an invalid "username"
    And I enter a "password"
    When I click the login button
    Then I should see an error message


  Scenario Outline: Successful Login
    Given I am on the login page
    When I enter a valid credentials "<username>" / "<password>"
    And I click the login button
    Then I should see a shopping cart
    Examples:
      | username                | password     |
      | standard_user           | secret_sauce |
      | problem_user            | secret_sauce |
      | performance_glitch_user | secret_sauce |


  Scenario Outline: Invalid Credentials
    Given I am on the login page
    When I enter an invalid credentials "<invalid_username>" / "<invalid_password>"
    And I click the login button
    Then I should see an error message
    Examples:
      | invalid_username | invalid_password |
      | locked_out_user  | secret_sauce     |
      | locked_out_user  | password         |
      | invalid_username | secret_sauce     |
      | username         | password         |


