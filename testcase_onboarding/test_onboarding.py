from time import sleep
from faker import Faker 
import pytest

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from conftest import URL

from locators import DonePageLocators, OnboardingLocators
from pages.all_listings.all_listings_page_object import AllListingsPageObject
from pages.explore_catalog.explore_catalogs_page_object import ExploreCatalogsPageObject
from pages.onboarding.onboarding_page_object import OnboardingPageObject
from pages.sign_up.sign_up_page_object import SignUpPageObject


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

    explore_catalog = ExploreCatalogsPageObject(driver)
    explore_catalog.wait_for_header()
    explore_catalog.click_on_browse()
    explore_catalog.click_on_all_listings()

    all_listings = AllListingsPageObject(driver)
    all_listings.wait_until_entering_the_page()
    all_listings.click_on_create_account()

    print('Can go to a non-homepage page and click "Create Account"')
    
    
    #Enter a new mail, a password and click submit button should redirect to onboarding page
    sign_up = SignUpPageObject(driver)
    try:
        sign_up.wait_until_entering_the_page()
    except:
        pytest.fail("Title of page does not contain 'Sign up' after clicking on 'Create Account' button")

    sign_up.set_email(faker.email())
    sign_up.set_password("UPPERlower4_")
    sign_up.click_continue_button()
    
    onboarding = OnboardingPageObject(driver)
    try:
        onboarding.wait_until_entering_the_page()
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
        onboarding.wait_until_entering_the_page()
    except TimeoutException:
        pytest.fail("After clicking continue button, and trying to go to the main"
                    + " page does not redirect to 'Onboarding' page")

    form = driver.find_element(By.TAG_NAME, "form")
    assert form, "Could not find a form"

    onboarding.set_first_name(faker.name())
    onboarding.set_last_name(faker.name())
    onboarding.submit()
    
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
