Feature: Validating adding items to cart and order completion

  Background:
    Given user is loggedin with valid credentials

  Scenario: Validating items in cart are retained after logout
    Given User is in the Home screen
    Then add 3 items to the cart
    Then check added items are available in the cart
    Then click on logout button
    Then user is logged out
    Then login again
    When clicked on cart icon
    Then previoulsy added items should be displayed

  Scenario: Validating user can place order
    Given User is in the Home screen
    Then add 2 items to the cart
    When clicked on Cart icon
    Then Cart information page is displayed
    When clicked on CheckOut button
    Then checkout information page is displayed
    Then enter details in the text fields
    When clicked on continue button
    Then Checkout Overview page is displayed
    Then check the total price equlal to the items price
    When clicked on Finish button
    Then Checkout Complete page is displayed
    When clicked on BackHome button
    Then Home page is displayed





