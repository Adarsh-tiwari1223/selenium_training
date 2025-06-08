from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    # Step 1: Navigate to the website
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    wait = WebDriverWait(driver, 10)

    # Step 2: Wait for the input field to be visible and enter text
    input_field = wait.until(EC.visibility_of_element_located((By.NAME, "my-text")))
    input_field.send_keys("testuser")

    # Step 3: Click a button (we'll click the submit button at the end)

    # Step 4: Select an option from a dropdown
    dropdown = Select(driver.find_element(By.NAME, "my-select"))
    dropdown.select_by_visible_text("Two")

    # Step 5: Select a checkbox
    checkbox = driver.find_element(By.ID, "my-check-1")
    checkbox.click()

    # Step 6: Simulate hover (optional)
    from selenium.webdriver.common.action_chains import ActionChains

    hover_element = driver.find_element(By.TAG_NAME, "h1")
    ActionChains(driver).move_to_element(hover_element).perform()

    # Step 7: Submit the form
    submit_button = driver.find_element(By.TAG_NAME, "button")
    submit_button.click()

    # Optional wait to let you see the result
    time.sleep(3)
    driver.save_screenshot("form_submission_result.png")

except (NoSuchElementException, TimeoutException) as e:
    print(f"Error during automation: {e}")

finally:
    driver.quit()
