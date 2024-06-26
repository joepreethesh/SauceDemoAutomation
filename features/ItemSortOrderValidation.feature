Feature: Validating default sort order of the product

  Background:
    Given user is loggedin with valid credentials

  Scenario: Validating default sort order
    Given User is in the Home screen
    Then Click on the default sort order
    Then validate Inventory Items are in the selected order

  Scenario: Validating inventory items are displayed in sort order - price high to low
    Given User is in the Home screen
    Then Click on the high to low order
    Then Inventory Items should be displayed in sort order - price high to low