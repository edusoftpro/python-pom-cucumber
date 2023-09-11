Feature: Logging to website

  Scenario: Successful login
    When I login using "seleniumremote@gmail.com"/"tester"
    Then I'm logged in