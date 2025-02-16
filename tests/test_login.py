import time
import json
import pytest
from selenium import webdriver
# from ..utils.config import USERNAME, PASSWORD
from utils.config import USERNAME, PASSWORD
from launch_openfin import launch_openfin

@pytest.fixture(scope="module")
def setup_browser():
    launch_openfin()  # Launch the OpenFin app
    time.sleep(60)  # Wait for the app to load
    driver = webdriver.Chrome()  # Adjust to your browser
    yield driver
    driver.quit()

def test_successful_login(setup_browser):
    driver = setup_browser
    driver.get("fins://fo-openfin.uat.apps.uk.mizuho-sc.com")  # Open the URL
    time.sleep(5)  # Wait for page to load

    username_input = driver.find_element_by_id("username")  # Adjust selector
    password_input = driver.find_element_by_id("password")  # Adjust selector
    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    driver.find_element_by_id("loginButton").click()  # Adjust selector

    time.sleep(5)  # Wait for login to process
    assert "Dashboard" in driver.title  # Check for successful login

def test_unsuccessful_login(setup_browser):
    driver = setup_browser
    driver.get("fins://fo-openfin.uat.apps.uk.mizuho-sc.com")
    time.sleep(5)

    username_input = driver.find_element_by_id("username")
    password_input = driver.find_element_by_id("password")
    username_input.send_keys("invalid_user")
    password_input.send_keys("wrong_password")
    driver.find_element_by_id("loginButton").click()

    time.sleep(5)
    assert "Invalid credentials" in driver.page_source  # Adjust expected text

def test_ui_elements_after_login(setup_browser):
    driver = setup_browser
    driver.get("fins://fo-openfin.uat.apps.uk.mizuho-sc.com")
    time.sleep(5)

    username_input = driver.find_element_by_id("username")
    password_input = driver.find_element_by_id("password")
    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    driver.find_element_by_id("loginButton").click()

    time.sleep(5)
    assert driver.find_element_by_id("dashboardElement").is_displayed()  # Check for UI element