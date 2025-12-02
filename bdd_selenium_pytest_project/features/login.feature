Feature: User Login

  Background:
    Given the application is available

  Scenario: Valid user logs in successfully
    When I open the login page
    And I enter valid username and password
    And I click the login button
    Then I should be redirected to the dashboard
