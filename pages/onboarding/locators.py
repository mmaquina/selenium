from selenium.webdriver.common.by import By


class OnboardingPageLocators():
    FORM_FIRST_NAME = (By.NAME, "firstName")
    FORM_LAST_NAME = (By.NAME, "lastName")
    FORM_SUBMIT = (By.XPATH, '//div[contains(text(), "Agree and Submit")]')
    FORM = (By.TAG_NAME, "form")
