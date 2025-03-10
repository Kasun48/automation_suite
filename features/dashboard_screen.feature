Feature: Dashboard Screen
  Background:
    Given the OpenFin application is launched
    When I enter valid credentials
    Then I should be logged in successfully

  Scenario: Open Dashboard Screen
    Given I am logged in to the application
    When I open the Dashboard screen
    Then the Dashboard screen should be displayed