from .locators import AllListingsPageLocators
from common import PageObject
from selenium.webdriver.support import expected_conditions as EC


class AllListingsPageObject(PageObject):

    def wait_until_entering_the_page(self):
        self._wait.until(EC.title_contains("All Listings"))

    def click_on_create_account(self):
        self.wait_for(AllListingsPageLocators.CREATE_ACCOUNT)
        create_account = self.find(AllListingsPageLocators.CREATE_ACCOUNT)
        create_account.click()