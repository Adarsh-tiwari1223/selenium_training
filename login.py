import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# ---------- Fixture: Setup and Teardown ----------
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    yield driver
    driver.quit()

# ---------- Test Case 1: Valid Login ----------
def test_valid_login(driver):
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")  # Correct password
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)

    assert "Congratulations" in driver.page_source
    assert "Logged In Successfully" in driver.find_element(By.TAG_NAME, "h1").text
    print("login Sucessfuly")

# ---------- Test Case 2: Invalid Login(password) ----------
def test_invalid_loginp(driver):
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("wrongpass")  # Wrong password
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)

    error_msg = driver.find_element(By.ID, "error").text
    assert "Your password is invalid!" in error_msg
    print("Your password is Invalid")
#-----------Test case 3: Invalid login(Username)---------------
def test_invalid_loginu(driver):
    driver.find_element(By.ID, "username").send_keys("wrn_user") # Wrong username
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    error_msg = driver.find_element(By.ID, "error").text
    assert "Your username is invalid!" in error_msg
    print("Your username is invalid!")