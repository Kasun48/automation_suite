Feature: Historical Trader Blotter Screen
  Background:
    Given the OpenFin application is launched
    When I enter valid credentials
    Then I should be logged in successfully

  Scenario: Open Historical Trader Blotter Screen
    Given I am logged in to the application
    When I open the Historical Trader Blotter screen
    Then the Historical Trader Blotter screen should be displayed