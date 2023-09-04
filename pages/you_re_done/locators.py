from selenium.webdriver.common.by import By


class DonePageLocators():
    SUCCESSFULLY_CREATED = By.XPATH, "//p[contains(text(), 'successfully created')]"
    YOU_RE_DONE = (By.XPATH, """//h3[contains(text(), "You're done!")]""")
