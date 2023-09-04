from .locators import ExploreCatalogPageLocators
from common import PageObject
from selenium.webdriver.support import expected_conditions as EC


class ExploreCatalogsPageObject(PageObject):

    def wait_for_header(self):
        """Waits for header to appear"""
        self.wait_for(ExploreCatalogPageLocators.HEADER_BROWSE)
    
    def click_on_browse(self):
        browse = self.find(ExploreCatalogPageLocators.HEADER_BROWSE)
        browse.click()

    def click_on_all_listings(self):
        self.wait_for(ExploreCatalogPageLocators.HEADER_ALL_LISTINGS)
        all_listings = self.find(ExploreCatalogPageLocators.HEADER_ALL_LISTINGS)
        all_listings.click()
