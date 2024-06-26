import time

from behave import *
from features.HelperClass.ProductPage import productPage


@given(u'User is in the Home screen')
def step_impl(context):
    context.product = productPage(context.driver)
    context.status = context.product.checkProductPageIsDisplayed()
    assert context.status, "Home screen is not displayed after login"
    time.sleep(3)

@then(u'Click on the default sort order')
def step_impl(context):
    context.product.clickOnSortOrder(0)
    time.sleep(3)

@then(u'validate Inventory Items are in the selected order')
def step_impl(context):
    inventoryList = context.product.getInventoryLists("invItemName_CLASSNAME")
    is_alphabetical_order = inventoryList == sorted(inventoryList)
    assert is_alphabetical_order, "Inventory items are not in selected order"
    time.sleep(3)

@then(u'Click on the high to low order')
def step_impl(context):
    context.product.clickOnSortOrder(3)
    time.sleep(3)

@then(u'Inventory Items should be displayed in sort order - price high to low')
def step_impl(context):
    inventoryPriceList = context.product.getInventoryLists("invPrice_CLASSNAME")
    is_descending_order = True
    for i in range(len(inventoryPriceList) - 1):
        current_price = float(inventoryPriceList[i][1:])
        next_price = float(inventoryPriceList[i + 1][1:])

        if current_price < next_price:
            is_descending_order = False
            break
    assert is_descending_order, "Inventory items are not displayed in price high to low order"
    time.sleep(3)