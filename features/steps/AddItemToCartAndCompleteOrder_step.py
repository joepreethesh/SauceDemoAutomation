import time
import re

from behave import *
from features.HelperClass.CartPage import cartPage
from features.HelperClass.LoginPage import loginPage
from features.HelperClass.ProductPage import productPage


@then(u'add 3 items to the cart')
def step_impl(context):
    context.cart = cartPage(context.driver)
    context.login = loginPage(context.driver)
    context.cart.addThreeItemToCart(3)
    time.sleep(2)

@then(u'check added items are available in the cart')
def step_impl(context):
    context.cartItems = context.cart.itemsAvailableInCart("invItemName_CLASSNAME")
    assert len(context.cartItems) != 0, "Added items are not available in cart"
    time.sleep(2)

@then(u'click on logout button')
def step_impl(context):
    context.login.clickOnHamburgerIcon()
    logoutButtonStatus = context.login.checkLogOutOptionIsDisplayed()
    assert logoutButtonStatus, "LogOut button is not displayed"
    context.login.clickLogoutButton()
    time.sleep(2)

@then(u'user is logged out')
def step_impl(context):
    screenStatus = context.login.loginScreenStatusAfterLogout()
    assert screenStatus, "Login screen is not displayed after logout"
    time.sleep(2)
@then(u'login again')
def step_impl(context):
    context.login.enterTextInUserNameAndPasswordField("standard_user")
    context.login.clickOnLoginButton()
    time.sleep(2)
@when(u'clicked on cart icon')
def step_impl(context):
    context.cart.clickCartButton()
    time.sleep(2)

@then(u'previoulsy added items should be displayed')
def step_impl(context):
    context.cartItemsAfterLogin = context.cart.itemsAvailableInCart("invItemName_CLASSNAME")
    assert len(context.cartItemsAfterLogin) != 0, "Added items are not available in cart after re-login"
    assert context.cartItems == context.cartItemsAfterLogin, "Added items are not euqla adter re-login"
    time.sleep(2)

@then(u'add 2 items to the cart')
def step_impl(context):
    context.cart = cartPage(context.driver)
    context.cart.addTwoItemsToCartWithPriceHighLow(2)
    time.sleep(2)

@then(u'Cart information page is displayed')
def step_impl(context):
    cartInfoPageStatus = context.cart.checkCartInfoPageIsDisplayed()
    assert cartInfoPageStatus, "Cart Info page is not displayed"
    time.sleep(2)

@when(u'clicked on CheckOut button')
def step_impl(context):
    context.cart.clickCheckoutButton()
    time.sleep(2)
@then(u'checkout information page is displayed')
def step_impl(context):
    checkoutInfoStatus = context.cart.checkCheckOutInfoPageIsDisplayed()
    assert checkoutInfoStatus, "Check Out Info page is not displayed"
    time.sleep(2)
@then(u'enter details in the text fields')
def step_impl(context):
    context.cart.enterTextInFirstName("Testing")
    context.cart.enterTextInLasttName("Test")
    context.cart.enterTextInPostalCode("560037")
    time.sleep(2)

@when(u'clicked on continue button')
def step_impl(context):
    context.cart.clickContinueButton()
    time.sleep(2)
@then(u'Checkout Overview page is displayed')
def step_impl(context):
    CheckOutOverviewStatus = context.cart.checkCheckOutOverviewPageIsDisplayed()
    assert CheckOutOverviewStatus, "Check Out overview page is not displayed"
    time.sleep(2)

@then(u'check the total price equlal to the items price excluding tax')
def step_impl(context):
    total_tax= 0.0
    totalCost = 0.0
    context.product = productPage(context.driver)
    inventoryPriceList = context.product.getInventoryLists("invPrice_CLASSNAME")
    total = context.cart.getTotalCost()
    print("total" + total)
    tax = context.cart.getTax()
    tax_match = re.search(r'\d+\.\d+', tax)
    totalCost_match = re.search(r'\d+\.\d+', total)
    if totalCost_match:
        totalCost = float(totalCost_match.group())

    if tax_match:
        total_tax = float(tax_match.group())

    print("inventoryPriceList", inventoryPriceList)

    for i in range(len(inventoryPriceList) - 1):
        current_price = float(inventoryPriceList[i][1:])
        next_price = float(inventoryPriceList[i + 1][1:])
    print("current_price", current_price)
    print("next price",  current_price)
    total_price = float(current_price + next_price)

    assert int(totalCost) == int(total_price), "Items price not matching with total cost"
    time.sleep(2)

@when(u'clicked on Finish button')
def step_impl(context):
    context.cart.clickFinishButton()
    time.sleep(2)
@then(u'Checkout Complete page is displayed')
def step_impl(context):
    checkOutCompleteStatus = context.cart.checkCheckOutCompletePageIsDisplayed()
    assert checkOutCompleteStatus, "Check out complete page is not displayed"
    time.sleep(2)
@when(u'clicked on BackHome button')
def step_impl(context):
    context.cart.clickBackHomeButton()
    time.sleep(2)
@then(u'Home page is displayed')
def step_impl(context):
    context.login = loginPage(context.driver)
    homeScreenStatus = context.login.loginHomeScreenStatus()
    assert homeScreenStatus, "Home screen is not displayed"
    time.sleep(2)