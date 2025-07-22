from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# Setup Chrome WebDriver
driver = webdriver.Chrome()

# ✅ Implicit Wait (applied globally)
driver.implicitly_wait(10)

# Open a sample login site
driver.get("https://practicetestautomation.com/practice-test-login/")

try:
    # ✅ Explicit Wait - wait for a specific element to be clickable
    message_input = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "username"))
    )
    message_input.clear()
    message_input.send_keys("student")

    # Click the 'Show Message' button
    show_button = driver.find_element(By.CSS_SELECTOR, "form#get-input > button")
    show_button.click()

    # ✅ Fluent Wait equivalent - wait for text to appear with polling
    wait = WebDriverWait(driver, 15, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
    output = wait.until(
        EC.text_to_be_present_in_element((By.ID, "display"), "Hello, Selenium!")
    )
    print("Test Passed: Message displayed correctly.")

except TimeoutException:
    print("Test Failed: Element not found or timeout occurred.")

# Cleanup
time.sleep(2)
driver.quit()
