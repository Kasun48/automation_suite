Feature: Position Manager Screen
  Background:
    Given the OpenFin application is launched
    When I enter valid credentials
    Then I should be logged in successfully

  Scenario: Open Position Manager Screen
    Given I am logged in to the application
    When I open the Position Manager screen
    Then the Position Manager screen should be displayed