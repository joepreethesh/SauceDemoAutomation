import os
import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from features.HelperClass.BasePage import BasePage
class productPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def checkProductPageIsDisplayed(self):
        time.sleep(5)
        productPageStatus = self.isElementDisplayed(By.CLASS_NAME, "Login", "loginHomePage_CLASSNAME")
        assert productPageStatus, "Product page is not displayed"
        return productPageStatus

    def clickOnSortOrder(self, index):
        self.selectItemFromDropdown(By.CLASS_NAME, "Products", "pdctSortContainer", index)
    def getInventoryLists(self, item):
        InventoryItemList = self.getInventoryItemNamesInProductScreen(By.CLASS_NAME, "Products", item)
        print(InventoryItemList)
        is_alphabetical_order = InventoryItemList == sorted(InventoryItemList)
        print(is_alphabetical_order)
        return InventoryItemList
        # total_tax = 0
        # elementText = self.driver.find_element(By.CLASS_NAME, "summary_tax_label").text
        # print(elementText)
        #
        # tax_match = re.search(r'\d+\.\d+', elementText)
        # if tax_match:
        #     total_tax = float(tax_match.group())
        #
        #
        # inventoryItems = []
        # inventoryItemList = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        # for element in inventoryItemList:
        #     inventoryItems.append(element.text)
        #
        # for i in range(len(inventoryItems) - 1):
        #     current_price = float(inventoryItems[i][1:])
        #     next_price = float(inventoryItems[i + 1][1:])
        # print(total_tax)
        # total_price = float(current_price + next_price)+total_tax
        #
        # print(total_price)




# current_directory = os.getcwd()
# print(current_directory)
# chrome_driver_path = os.path.join('/Users/joe/AutomationAssignment', 'webdriver', 'chromedriver')
# print(chrome_driver_path)
# driver = webdriver.Chrome()
# driver.get("https://www.saucedemo.com")
# driver.maximize_window()
# helper = productPage(driver)
# # helper.clickOnSortOrder(3)
# helper.getInventoryLists()