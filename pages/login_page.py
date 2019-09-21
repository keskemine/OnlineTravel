from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from base.selenium_driver import SeleniumDriver

class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

#Locators

    _account="//button[@id='header-account-menu']"
    _sign_in="//a[@id='account-signin']"
    _email_address="//input[@id='gss-signin-email']"
    _password="//input[@id='gss-signin-password']"
    _signin_btn="//button[@id='gss-signin-submit']"
    _forgot_password="//a[@id='gss-go-to-forgot-password']"
    _reset_password="//button[@id='gss-forgot-password-submit']"



    def clickAccount(self):
        self. elementClick(self._account, locatorType="xpath")

    def clickSign_in(self):
        self.elementClick(self._sign_in,locatorType="xpath")

    def sendkeyEmail(self, email):
        self.sendKeys(email, self._email_address, locatorType="xpath")

    def sendkeyPassword(self, password):
        self.sendKeys(password, self._password,locatorType="xpath")

    def clickSignInBtn(self):
        self.elementClick(self._signin_btn,locatorType="xpath")

    def clickForgotPassword(self):
        self.elementClick(self._forgot_password,locatorType="xpath")

    def clickResetPassword(self):
        self.elementClick(self._reset_password, locatorType="xpath")



    def account(self):
        self.clickAccount()
        time.sleep(2)

    def signIn(self):
        self.clickSign_in()
        time.sleep(2)

    def email(self,email):
        self.sendkeyEmail(email)
        time.sleep(2)

    def forgotPassword(self):
        self.clickForgotPassword()
        time.sleep(2)

    def resetPassword(self):
        self.clickResetPassword()
        time.sleep(2)

    def password(self, password):
        self.sendkeyPassword(password)
        time.sleep(2)

    def signInBtn(self):
        self.clickSignInBtn()
        time.sleep(2)

    def blankemail(self,email,password):
        self.clickAccount()
        time.sleep(2)
        self.clickSign_in()
        time.sleep(2)
        self.sendkeyEmail(email)
        time.sleep(2)
        self.sendkeyPassword(password)
        time.sleep(2)
        self.clickSignInBtn()
        time.sleep(2)


    def blankPassword(self,email,password):
        self.clickAccount()
        time.sleep(2)
        self.clickSign_in()
        time.sleep(2)
        self.sendkeyEmail(email)
        time.sleep(2)
        self.sendkeyPassword(password)
        time.sleep(2)
        self.clickSignInBtn()
        time.sleep(2)


    def invalidEmail(self,email, password):
        self.clickAccount()
        time.sleep(2)
        self.clickSign_in()
        time.sleep(2)
        self.sendkeyEmail(email)
        time.sleep(2)
        self.sendkeyPassword(password)
        time.sleep(2)
        self.clickSignInBtn()
        time.sleep(2)


















