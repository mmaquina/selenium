from selenium.webdriver.common.by import By


class MainPageLocators():
    """A class for main page locators. All main page locators should come here"""

    HEADER = (By.XPATH, "//div[contains(@class, 'z-header')]")
    HEADER_BROWSE = (By.XPATH, "//div[contains(@class, 'z-header')]//p[contains(text(), 'Browse')]")
    HEADER_ALL_LISTINGS = (By.XPATH, "//div[contains(@class,'z-header')]//a[contains(text(), 'All Listings')]")
    CREATE_ACCOUNT = By.XPATH, "//div[contains(text(),'Create Account')]"


class OnboardingLocators():
    FORM_FIRST_NAME = (By.NAME, "firstName")
    FORM_LAST_NAME = (By.NAME, "lastName")
    FORM_SUBMIT = (By.XPATH, '//div[contains(text(), "Agree and Submit")]')


class DonePageLocators():
    SUCCESSFULLY_CREATED = By.XPATH, "//p[contains(text(), 'successfully created')]"
    YOU_RE_DONE = (By.XPATH, """//h3[contains(text(), "You're done!")]""")
