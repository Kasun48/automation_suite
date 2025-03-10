Feature: Comments Screen
  Background:
    Given the OpenFin application is launched
    When I enter valid credentials
    Then I should be logged in successfully

  Scenario: Open Comments Screen
    Given I am logged in to the application
    When I open the Comments screen
    Then the Comments screen should be displayed