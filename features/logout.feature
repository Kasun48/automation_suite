Feature: Logout from Mizuho OpenFin Application

  Scenario: Successful logout
    Given I am logged in to the application
    When I log out
    Then I should be logged out successfully