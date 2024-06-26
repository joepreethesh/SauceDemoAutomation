import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from features.HelperClass.BasePage import BasePage


class cartPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def addThreeItemToCart(self, cartItem):
        self.addItemsToCart(By.CSS_SELECTOR, "Cart", "addToCartButton_CSSSELECTOR", cartItem)
    def clickCartButton(self):
        self.click(By.CLASS_NAME, "Cart", "cartIcon_CLASSNAME")

    def itemsAvailableInCart(self, item):
        self.clickCartButton()
        InventoryItemList = self.getInventoryItemNamesInProductScreen(By.CLASS_NAME, "Products", item)
        return InventoryItemList

    def addTwoItemsToCartWithPriceHighLow(self, cartItem):
        self.selectItemFromDropdown(By.CLASS_NAME, "Products", "pdctSortContainer", 3)
        self.addItemsToCart(By.CSS_SELECTOR, "Cart", "addToCartButton_CSSSELECTOR", cartItem)

    def checkCartInfoPageIsDisplayed(self):
        elementStatus = self.isElementDisplayed(By.CSS_SELECTOR, "Cart", "cartInfo_CSSSELECTOR")
        return elementStatus

    def clickCheckoutButton(self):
        self.click(By.CSS_SELECTOR, "Cart", "cartInfo_CSSSELECTOR")

    def checkCheckOutInfoPageIsDisplayed(self):
        elementStatus = self.isElementDisplayed(By.ID, "Checkout", "continueButton_ID")
        return elementStatus
    def enterTextInFirstName(self,firstNameText):
        self.sendKeys(By.ID, "Checkout", "firstName_ID", firstNameText)
    def enterTextInLasttName(self, lasttNameText):
        self.sendKeys(By.ID, "Checkout", "lastName_ID", lasttNameText)
    def enterTextInPostalCode(self, postalCodeText):
        self.sendKeys(By.ID, "Checkout", "postalCode_ID", postalCodeText)

    def clickContinueButton(self):
        self.click(By.ID, "Checkout", "continueButton_ID")
    def checkCheckOutOverviewPageIsDisplayed(self):
        elementStatus = self.isElementDisplayed(By.ID, "Checkout", "finishButton_ID")
        return elementStatus

    def getTotalCost(self):
        elementText = self.getText(By.CSS_SELECTOR, "Checkout", "totalCost_CSSSELECTOR")
        return elementText

    def clickFinishButton(self):
        self.click(By.ID, "Checkout", "finishButton_ID")

    def checkCheckOutCompletePageIsDisplayed(self):
        elementStatus = self.isElementDisplayed(By.ID, "Checkout", "backHomeButton_ID")
        return elementStatus

    def clickBackHomeButton(self):
        self.click(By.ID, "Checkout", "backHomeButton_ID")

    def getTax(self):
        taxValue = self.getText(By.CLASS_NAME, "Checkout", "taxValue_CLASSNAME")
        return taxValue


# current_directory = os.getcwd()
# chrome_driver_path = os.path.join(current_directory, 'webdriver', 'chromedriver')
# driver = webdriver.Chrome()
# driver.get("https://www.saucedemo.com")
# driver.maximize_window()
# helper = cartPage(driver)
# # helper.clickOnSortOrder(3)
# helper.getTotalCost()