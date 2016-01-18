# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from robot.libraries.BuiltIn import BuiltIn


locators = {"login_button": "//div[@title='Войти']"
            , "email_field": "//input[@placeholder='Электронная почта']"
            , "password_field": "//input[@placeholder='Пароль']"
            , "submit_credentials_button": "//button[contains(text(),'Войти')]"
            , "user_email_info": "//div[@class='tools__btn tools__user']"}


def selenium_lib():
    return BuiltIn().get_library_instance("Selenium2Library")


class MainPage(object):

    def press_login_button(self):
        selenium_lib().click_element(locators["login_button"])
        selenium_lib().wait_until_page_contains_element(locators["email_field"])
        selenium_lib().wait_until_page_contains_element(locators["password_field"])

    def fill_email_field(self, text):
        selenium_lib().input_text(locators["email_field"], text)

    def fill_password_field(self, text):
        selenium_lib().input_text(locators["password_field"], text)

    def press_submit_credentials_button(self):
        selenium_lib().click_element(locators["submit_credentials_button"])
        selenium_lib().wait_until_page_contains_element(locators["user_email_info"])



