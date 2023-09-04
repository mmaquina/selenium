from selenium.webdriver.common.by import By


class SignUpPageLocators():
    FORM = (By.TAG_NAME, "form")
    FORM_EMAIL = (By.NAME, "email")
    FORM_PASSWORD = (By.NAME, "password")
    FORM_SUBMIT = (By.NAME, "action")