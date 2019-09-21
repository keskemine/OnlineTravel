from selenium import webdriver
from pages.login_page import LoginPage
from base.webdriverfactory import WebDriverFactory

import unittest
import allure
import pytest
import time

class LoginTest(unittest.TestCase):# LOGIN PART
    global webdriver

    def test_login(self):
        wd = WebDriverFactory(browser= "chrome.driver")
        driver = wd.getWebDriverInstance()
        lt = LoginPage(driver)

        # Click and verify account
        lt.account()
        element = driver.find_element_by_xpath("//button[@id='header-account-menu']")
        if element.is_enabled():
            print("Test case TC001: Pass")
        else:
            print("Test Case TC001: Fail")

        # Click and verify Sign in
        lt.signIn()
        element = driver.find_element_by_xpath("//a[@id='account-signin']")
        if element.is_enabled():
            print("Test Case Tc002: Pass")
        else:
            print("Test Case TC002: Fail")

        # Send email and verify email
        lt.email("rosemily.johnson@gmail.com")
        email = driver.find_element_by_xpath("//input[@id='gss-signin-email']")
        if email.is_enabled():
            print("Test Case Tc003: Pass")
        else:
            print("Test Case TC003: Fail")

        # # Click and verify 'Forgot Password Button'
        # lt.forgotPassword()
        # heading = driver.find_element_by_xpath("//h2[@id='gss-forgot-password-heading']")
        # print(heading.text)
        # if heading.text=="Reset your password":
        #     print("Test Case TC004: Pass")
        # else:
        #     print("Test Case TC004: Fail ")

        # Send Password and Verify
        lt.password("Ej12345679*")
        password = driver.find_element_by_xpath("//input[@id='gss-signin-password']")
        if password.is_enabled():
            print("Test Case TC004: Pass")
        else:
            print("Test Case TC004: Fail")


        # Click and verify Sign In Button
        lt.signInBtn()
        header_account = driver.find_element_by_xpath("//button[@id='header-account-menu-signed-in']")
        if header_account.is_enabled():
            print("Test Case TC005: Pass")
        else:
            print("Test Case TC005: Fail")

    def test_blank_email(self):
        wd = WebDriverFactory(browser="chrome.driver")
        driver = wd.getWebDriverInstance()
        lt = LoginPage(driver)

        #Verify that the email field must be fill out
        lt.blankemail("","Ej12345679*")
        message = driver.find_element_by_xpath("//p[@id='signInEmailErrorMessage']")
        print(message.text)
        if message.text=="Please enter an email address":
            print("Test Case TC006: Pass")
        else:
            print("Test Case TC006: Fail")


    def test_blank_password(self):
        wd = WebDriverFactory(browser="chrome.driver")
        driver = wd.getWebDriverInstance()
        lt= LoginPage(driver)

        #Verify that the password field must be fill out
        lt.blankPassword("rosemily.johnson@gmail.com","")
        message = driver.find_element_by_xpath("//p[@id='signInPasswordErrorMessage']")
        print(message.text)
        if message.text=="Please enter a password":
            print("Test Case TC007: Pass")
        else:
            print("Test Case TC007: Fail")


    def test_validation(self):
        wd= WebDriverFactory(browser="chrome.driver")
        driver = wd.getWebDriverInstance()
        lt = LoginPage(driver)

        #Verify that password and email must be correct
        lt.invalidEmail("rosemily.johnson@gmail.com","Ej12345679")
        message = driver.find_element_by_xpath("//div[@id='gss-signin-incorrect-email-or-password']")
        print(message.text)
        if message.text=="You may have entered an unknown email address or an incorrect password":
            print("Test Case TC008: Pass" )
        else:
            print("Test Case TC008: Fail")

