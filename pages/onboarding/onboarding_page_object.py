from .locators import OnboardingPageLocators
from common import PageObject
from selenium.webdriver.support import expected_conditions as EC


class OnboardingPageObject(PageObject):

    def wait_until_entering_the_page(self):
        self._wait.until(EC.title_contains("Onboarding"))
        return self.wait_for(OnboardingPageLocators.FORM)

    def set_first_name(self, name):
        first_name = self.find(OnboardingPageLocators.FORM_FIRST_NAME)
        first_name.send_keys(name)

    def set_last_name(self, name):
        last_name = self.find(OnboardingPageLocators.FORM_LAST_NAME)
        last_name.send_keys(name)
    
    def submit(self):
        submit_button = self.find(OnboardingPageLocators.FORM_SUBMIT)
        submit_button.click()