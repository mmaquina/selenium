from time import sleep
from faker import Faker 
import pytest

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from conftest import URL

from locators import DonePageLocators, MainPageLocators, OnboardingLocators


faker = Faker()


def test__onboarding_process(setup_teardown):
    """
    Go to a non-homepage page and click "Create Account"
    Enter a new email address and password.
    Get redirected to the onboarding page
    Do not complete the onboarding process. Close your tab.
    Open up a new tab and go to the home page.
    You should be automatically redirected to the onboarding process.
    Complete the onboarding process
    The "You're done" page is shown.
    You should be redirected to the previous page you were on before signup.
    """
    driver, wait = setup_teardown

    try:
        wait.until(EC.visibility_of_element_located(MainPageLocators.HEADER))
    except TimeoutException:
        pytest.fail("Cannot find the header in the main page")

    browse = driver.find_element(*MainPageLocators.HEADER_BROWSE)
    browse.click()

    all_listings = wait.until(EC.visibility_of_element_located(MainPageLocators.HEADER_ALL_LISTINGS))
    all_listings.click()
    wait.until(EC.title_contains("All Listings"))

    create_account = driver.find_element(*MainPageLocators.CREATE_ACCOUNT)
    create_account.click()
    print('Can go to a non-homepage page and click "Create Account"')
    assert "Sign up" in driver.title, "Title of page does not contain 'Sign up' after clicking on 'Create Account' button"


    #Enter a new mail, a password and click submit button should redirect to onboarding page
    form = driver.find_element(By.TAG_NAME, "form")
    email = form.find_element(By.NAME, "email")
    email.send_keys(faker.email())
    password = form.find_element(By.NAME, "password")
    password.send_keys("UPPERlower4_")

    continue_button = form.find_element(By.NAME, "action")
    continue_button.click()
    try:
        wait.until(EC.title_contains("Onboarding"))
    except TimeoutException:
        pytest.fail("After clicking continue button, next page does not contain 'Onboarding' in the title")


    # After closing the tab without completing the process
    # other pages redirect to the onboarding page
    
    # Open a new tab using JavaScript (this opens a blank tab)
    driver.execute_script("window.open('', '_blank');")

    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[1])

    driver.get(URL)
    try:
        wait.until(EC.title_contains("Onboarding"))
    except TimeoutException:
        pytest.fail("After clicking continue button, and trying to go to the main"
                    + " page does not redirect to 'Onboarding' page")

    form = driver.find_element(By.TAG_NAME, "form")
    assert form, "Could not find a form"

    first_name = form.find_element(*OnboardingLocators.FORM_FIRST_NAME)
    first_name.send_keys(faker.name())
    last_name = form.find_element(*OnboardingLocators.FORM_LAST_NAME)
    last_name.send_keys(faker.name())
    submit = driver.find_element(*OnboardingLocators.FORM_SUBMIT)
    submit.click()

    try:
        wait.until(EC.visibility_of_element_located(DonePageLocators.YOU_RE_DONE))
    except TimeoutException:
        # If the element is not found, the assertion fails
        pytest.fail("You are done page not shown")
    assert driver.find_element(
        *DonePageLocators.SUCCESSFULLY_CREATED
        ), "Couldn't find a paragraph containing 'successfully created"
    
    # You should be redirected to the previous page you were on before BEING REDIRECTED TO ONBOARDING.
    assert wait.until(EC.title_contains("Explore Catalog")), "Failed to get redirected to Explore"
