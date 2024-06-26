import time

from behave import *

from features.HelperClass.LoginPage import loginPage

@given(u'web page is launched')
def step_impl(context):
    context.login = loginPage(context.driver)
    context.status = context.login.checkWebPageIsDisplayed()
    assert context.status, "Web page is not displayed"
    time.sleep(3)

@then(u'User enters valid credentials "{user}"')
def step_impl(context, user):
    context.login.enterTextInUserNameAndPasswordField(user)
    time.sleep(3)
@then(u'home screen is displayed')
def step_impl(context):
    homeScreenStatus = context.login.loginHomeScreenStatus()
    assert homeScreenStatus, "Unable to login"
    time.sleep(3)
@when(u'clciked on Hamburger menu icon')
def step_impl(context):
    context.login.clickOnHamburgerIcon()
    time.sleep(3)
@then(u'Logout option should be displayed')
def step_impl(context):
    logoutButtonStatus = context.login.checkLogOutOptionIsDisplayed()
    assert logoutButtonStatus, "LogOut button is not displayed"
    time.sleep(3)
@when(u'clicked on LogOut button')
def step_impl(context):
    context.login.clickLogoutButton()
    time.sleep(3)

@then(u'Login screen is displayed')
def step_impl(context):
    screenStatus = context.login.loginScreenStatusAfterLogout()
    assert screenStatus, "Login screen is not displayed after logout"
    time.sleep(3)
@then(u'User clicks on Login Button')
def step_impl(context):
    context.login.clickOnLoginButton()
    time.sleep(3)
@then(u'User enters Invalid credentials "{Invaliduser}"')
def step_impl(context, Invaliduser):
    context.login.enterTextInUserNameAndPasswordField(Invaliduser)
    time.sleep(3)

@then(u'Error message is displayed')
def step_impl(context):
    errorPromptStatus = context.login.checkErrorMessageForInvalidLogin()
    assert errorPromptStatus, "Error message is not displayed for Invalid Login"
    time.sleep(3)

