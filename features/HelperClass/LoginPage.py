import time
from selenium.webdriver.common.by import By
from features.HelperClass.BasePage import BasePage


class loginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def checkWebPageIsDisplayed(self):
        elementStatus = self.isElementDisplayed(By.ID, "Login", "loginButton_ID")
        print(elementStatus)
        return elementStatus

    def enterTextInUserNameAndPasswordField(self, user):
        self.enterText(By.ID, "Login", "userNameTextField_ID", "passwordTextField_ID",user)

    def clickOnLoginButton(self):
        self.click(By.ID, "Login", "loginButton_ID")

    def loginHomeScreenStatus(self):
        homeScreenStatus = self.isElementDisplayed(By.CLASS_NAME, "Login", "loginHomePage_CLASSNAME")
        return homeScreenStatus

    def clickOnHamburgerIcon(self):
        self.click(By.ID, "Login", "hamburgerIcon_ID")

    def checkLogOutOptionIsDisplayed(self):
        time.sleep(3)
        logoutButtonStatus = self.isElementDisplayed(By.ID, "Login", "logout_ID")
        return logoutButtonStatus

    def clickLogoutButton(self):
        self.click(By.ID, "Login", "logout_ID")

    def loginScreenStatusAfterLogout(self):
        loginScreenStatus = self.isElementDisplayed(By.ID, "Login", "loginButton_ID")
        return loginScreenStatus

    def checkErrorMessageForInvalidLogin(self):
        errorMessageStatus = self.isElementDisplayed(By.CLASS_NAME, "Login", "errorPrompt_CLASSNAME")
        return errorMessageStatus





