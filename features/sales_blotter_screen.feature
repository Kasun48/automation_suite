Feature: Sales Blotter Screen
  Background:
    Given the OpenFin application is launched
    When I enter valid credentials
    Then I should be logged in successfully

  Scenario: Open Sales Blotter Screen
    Given I am logged in to the application
    When I open the Sales Blotter screen
    Then the Sales Blotter screen should be displayed