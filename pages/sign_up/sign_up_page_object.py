from .locators import SignUpPageLocators
from common import PageObject
from selenium.webdriver.support import expected_conditions as EC
import pytest


class SignUpPageObject(PageObject):

    def wait_until_entering_the_page(self):
        try:
            self._wait.until(EC.title_contains("Sign up"))
        except:
            pytest.fail("Title of page does not contain 'Sign up' after clicking on 'Create Account' button")

    def set_email(self, email):
        email_input = self.find(SignUpPageLocators.FORM_EMAIL)
        email_input.send_keys(email)
    
    def set_password(self, password):
        password_input = self.find(SignUpPageLocators.FORM_PASSWORD)
        password_input.send_keys(password)

    def click_continue_button(self):
        continue_button = self.find(SignUpPageLocators.FORM_SUBMIT)
        continue_button.click()