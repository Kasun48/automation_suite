Feature: User Logout
  Background:
    Given the OpenFin application is launched
    When I enter valid credentials
    Then I should be logged in successfully
    
  Scenario: Successful logout
    Given I am logged in to the application
    When I log out
    Then I should be logged out successfully