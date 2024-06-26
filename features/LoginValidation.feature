Feature: Validating Login functionality for Standard_User and Performance_Glitch_User

  Background:
    Given web page is launched

  Scenario Outline:
    Then User enters valid credentials "<user>"
    Then User clicks on Login Button
    Then home screen is displayed
    When clciked on Hamburger menu icon
    Then Logout option should be displayed
    When clicked on LogOut button
    Then Login screen is displayed
    Examples:
    |user|
    |standard_user|
    |performance_glitch_user|

  Scenario Outline:
    Then User enters Invalid credentials "<Invaliduser>"
    Then User clicks on Login Button
    Then Error message is displayed
    Examples:
    |Invaliduser|
    |locked_out_user|







