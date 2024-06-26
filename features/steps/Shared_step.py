from behave import *
from features.HelperClass.LoginPage import loginPage

@given(u'user is loggedin with valid credentials')
def step_impl(context):
    context.login = loginPage(context.driver)
    context.webPageStatus = context.login.checkWebPageIsDisplayed()
    if context.webPageStatus:
        context.login.enterTextInUserNameAndPasswordField("standard_user")
        context.login.clickOnLoginButton()
