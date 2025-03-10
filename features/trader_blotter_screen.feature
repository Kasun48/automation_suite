Feature: Trader Blotter Screen
  Background:
    Given the OpenFin application is launched
    When I enter valid credentials
    Then I should be logged in successfully

  Scenario: Open Trader Blotter Screen
    Given I am logged in to the application
    When I open the Trader Blotter screen
    Then the Trader Blotter screen should be displayed