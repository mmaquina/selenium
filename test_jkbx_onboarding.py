import os
from time import sleep
from faker import Faker 

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from conftest import URL

faker = Faker()



def test__go_to_non_home_page_and_click_create_account_button(setup_teardown):
    """Test if Create Account buton works when navigating first to All Listings"""
    driver, wait = setup_teardown

    header = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'z-header')]")))
    browse = header.find_element(By.XPATH, "//p[contains(text(), 'Browse')]")
    browse.click()

    all_listings = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'z-header')]//a[contains(text(), 'All Listings')]")))
    all_listings.click()
    wait.until(EC.title_contains("All Listings"))
 
    create_account = driver.find_element(By.XPATH, "//div[contains(text(),'Create Account')]")
    create_account.click()
    print('Can go to a non-homepage page and click "Create Account"')
    assert "Sign up" in driver.title, "Title of page does not contain 'Sign up' after clicking on 'Create Account' button"
    

    form = driver.find_element(By.TAG_NAME, "form")
    email = form.find_element(By.NAME, "email")
    email.send_keys(faker.email())
    password = form.find_element(By.NAME, "password")
    password.send_keys("UPERlower4_")
    continue_button = form.find_element(By.NAME, "action")
    continue_button.click()
    wait.until(EC.title_contains("Onboarding"))

    # Open a new tab using JavaScript (this opens a blank tab)
    driver.execute_script("window.open('', '_blank');")

    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[1])

    driver.get(URL)
    wait.until(EC.title_contains("Onboarding"))

    form = driver.find_element(By.TAG_NAME, "form")
    first_name = form.find_element(By.NAME, "firstName")
    first_name.send_keys(faker.name())
    last_name = form.find_element(By.NAME, "lastName")
    last_name.send_keys(faker.name())
    submit = driver.find_element(By.XPATH, '//div[contains(text(), "Agree and Submit")]')

    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'You are done!)]")))
    except NoSuchElementException:
        # If the element is not found, the assertion fails
        pytest.fail("You are done page not shown")