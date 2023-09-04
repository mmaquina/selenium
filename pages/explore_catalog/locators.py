from selenium.webdriver.common.by import By


class ExploreCatalogPageLocators():
    HEADER = (By.XPATH, "//div[contains(@class, 'z-header')]")
    HEADER_BROWSE = (By.XPATH, "//div[contains(@class, 'z-header')]//p[contains(text(), 'Browse')]")
    HEADER_ALL_LISTINGS = (By.XPATH, "//div[contains(@class,'z-header')]//a[contains(text(), 'All Listings')]")
    CREATE_ACCOUNT = By.XPATH, "//div[contains(text(),'Create Account')]"
