Feature: Pass and failed logins

  Scenario Outline: pass logins with valid username and password
    Given I open chrome browser
    When I go to the website https://www.saucedemo.com/
    And input username "<username>" and password "<password>"
    And click login button
    Then I should login and the page will include "Products"

    Examples:
      | username                | password     |
      | standard_user           | secret_sauce |
      | problem_user            | secret_sauce |
      | performance_glitch_user | secret_sauce |

  Scenario Outline: failed logins with invalid username or password
    Given I open chrome browser
    When I go to the website https://www.saucedemo.com/
    And input username "<username>" and password "<password>"
    And click login button
    Then I should not login and the page will include "<expect_error>"

    Examples:
      | username        | password       | expect_error                                                              |
      | standard_user   |                | Epic sadface: Password is required                                        |
      |                 | secret_sauce   | Epic sadface: Username is required                                        |
      | wrong_username  | secret_sauce   | Epic sadface: Username and password do not match any user in this service |
      | standard_user   | wrong_password | Epic sadface: Username and password do not match any user in this service |
      | locked_out_user | secret_sauce   | Epic sadface: Sorry, this user has been locked out.                       |

  Scenario: login as a valid user
    Given I login as a valid user
    Then I should login and the page will include "Products"