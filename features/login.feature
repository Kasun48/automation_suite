Feature: User Login

  Scenario: Successful login
    Given the OpenFin application is launched
    When I enter valid credentials
    Then I should be logged in successfully

  Scenario: Unsuccessful login with invalid credentials
    Given the OpenFin application is launched
    When I enter invalid credentials
    Then I should see an error message