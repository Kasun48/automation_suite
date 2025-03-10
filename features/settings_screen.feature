Feature: Settings Screen
  Background:
    Given the OpenFin application is launched
    When I enter valid credentials
    Then I should be logged in successfully

  Scenario: Open Settings Screen
    Given I am logged in to the application
    When I open the Settings screen
    Then the Settings screen should be displayed