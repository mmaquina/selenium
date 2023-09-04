from .locators import DonePageLocators
from common import PageObject
from selenium.webdriver.support import expected_conditions as EC
import pytest


class DonePageObject(PageObject):
    def wait_until_loaded(self):
        self.wait_for(DonePageLocators.YOU_RE_DONE)
        self.find(DonePageLocators.SUCCESSFULLY_CREATED)