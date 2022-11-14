Feature: Inventory page features

  Background: Login as a valid user
    Given I login as a valid user
    Then I should login and the page will include "Products"

  Scenario: Add product to the shopping cart
    Given a list of products
      | product                           |
      | Sauce Labs Bolt T-Shirt           |
      | Sauce Labs Onesie                 |
#      | Sauce Labs Backpack               |
      | Sauce Labs Bike Light             |
#      | Sauce Labs Fleece Jacket          |
      | Test.allTheThings() T-Shirt (Red) |

    When I add each product to the shopping cart
    And click the shopping cart icon to go to the cart page
    Then I should go to the cart page and see the products are in the shopping cart
