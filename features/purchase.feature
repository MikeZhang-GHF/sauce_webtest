Feature: Purchase product process

  Background: Login as a valid user
    Given I login as a valid user
    Then I should login and the page will include "Products"

  Scenario: Add a list of products to the shopping cart
    Given a list of products
      | product                           |
      | Sauce Labs Bolt T-Shirt           |
      | Sauce Labs Onesie                 |
      | Sauce Labs Backpack               |
      | Sauce Labs Bike Light             |
      | Sauce Labs Fleece Jacket          |
      | Test.allTheThings() T-Shirt (Red) |
    When I add each product to the shopping cart
    And click the shopping cart icon to go to the cart page
    And click the checkout button to checkout step one page
    And input firstname, lastname, and zipcode
    And click continue button to checkout step two page
    And click finish button to checkout complete page
    Then I should go to the checkout complete page and see the checkout complete