from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


WAIT_TIME = 20


class PageObject:

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, WAIT_TIME)
    
    def wait_for(self, locator):
        return self._wait.until(EC.presence_of_all_elements_located(locator))
    
    def find(self, locator):
        return self.driver.find_element(*locator)

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""

        driver = obj.driver
        WebDriverWait(driver, WAIT_TIME).until(
            lambda driver: driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""

        driver = obj.driver
        WebDriverWait(driver, WAIT_TIME).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")
