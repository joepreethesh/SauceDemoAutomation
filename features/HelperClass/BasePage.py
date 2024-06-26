import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utilities import ConfigReader
class BasePage():
    def __init__(self, driver):
        self.driver = driver
    def isElementDisplayed(self, locatorID, configFileName, locatorName):
        try:
            self.driver.find_element(locatorID, ConfigReader.readConfig(configFileName, locatorName))
            return True
        except:
            return False

    def waitUntilElementIsDisplayed(self, locatorID, configFileName, UserNamelocator, PasswordLocator):
        pass

    def enterText(self,locatorID, configFileName, userNameLocator, passwordLocator, userId):
        loginCredentialsElement = self.driver.find_element(By.ID, ConfigReader.readConfig(configFileName, "userNameList_ID"))
        credentials_text = loginCredentialsElement.text
        usernames = [username.strip() for username in credentials_text.split('\n')[1:]]
        if userId == "standard_user":
            userNameTextField = self.driver.find_element(locatorID, ConfigReader.readConfig(configFileName, userNameLocator))
            userNameTextField.clear()
            userNameTextField.send_keys(usernames[0])
        elif userId == "performance_glitch_user":
            userNameTextField = self.driver.find_element(locatorID,
                                                         ConfigReader.readConfig(configFileName, userNameLocator))
            userNameTextField.clear()
            userNameTextField.send_keys(usernames[-1])

        passwordElement = self.driver.find_element(By.CLASS_NAME, 'login_password')
        password_text = passwordElement.text
        passwordText = password_text.split(':')[1].strip()
        passwordTextField = self.driver.find_element(locatorID,
                                                     ConfigReader.readConfig(configFileName, passwordLocator))
        passwordTextField.clear()
        passwordTextField.send_keys(passwordText)

    def click(self, locator, configFileName, locatorName):
        self.driver.find_element(locator, ConfigReader.readConfig(configFileName,locatorName)).click()

    def selectItemFromDropdown(self, locator, configFileName, locatorName, index):
        select_element = self.driver.find_element(locator, ConfigReader.readConfig(configFileName,locatorName))
        select_element.click()
        select = Select(select_element)
        time.sleep(2)
        select.select_by_index(index)

    def getInventoryItemNamesInProductScreen(self, locator, configFileName, locatorName):
        inventoryItems = []
        inventoryItemList = self.driver.find_elements(locator, ConfigReader.readConfig(configFileName,locatorName))
        for element in inventoryItemList:
            inventoryItems.append(element.text)
        return inventoryItems

    def addItemsToCart(self, locator, configFileName, locatorName, cartItems):
        addToCartButtonList = self.driver.find_elements(locator, ConfigReader.readConfig(configFileName, locatorName))
        if cartItems == 3:
            for i in range(min(cartItems, len(addToCartButtonList))):
                addToCartButtonList[i].click()

        if cartItems == 2:
            addToCartButtonList[0].click()
            addToCartButtonList[-1].click()

    def sendKeys(self, locator, configFileName, locatorName, InputText):
        textfield = self.driver.find_element(locator, ConfigReader.readConfig(configFileName, locatorName))
        textfield.send_keys(InputText)

    def getText(self, locator, configFileName, locatorName):
        elementText = self.driver.find_element(locator, ConfigReader.readConfig(configFileName, locatorName))
        return elementText.text

















