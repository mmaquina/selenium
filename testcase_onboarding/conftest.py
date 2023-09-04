import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

URL = "http://staging.jkbx.com/?_vercel_share=QmPV8y4Nz8iGustBDS7ENtbyJMcx5yeE"

def pytest_runtest_protocol(item, nextitem):
    # Access the test function and its docstring
    test_function = item.function
    print(f"\nTesting function: {test_function.__name__}")
    docstring = test_function.__doc__
    if docstring:
        # Print the docstring if it exists
        print(f"{docstring}\n")
    # Continue with the test execution
    return None


@pytest.fixture(scope="module")
def setup_teardown():
    # Setup code - Initialize the WebDriver
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.maximize_window()   

    yield driver  # This is the value that will be passed to the test function

    # Teardown code - Close the WebDriver
    driver.quit()
