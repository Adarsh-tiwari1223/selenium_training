from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoAlertPresentException
from time import sleep
# Navigate to the login page and wait for the page to load completely.
#
# Enter a username and password in the respective fields.
#
# Click the "Login" button to submit the login form, triggering an AJAX request.
#
# Wait for the loading spinner to disappear, indicating the AJAX request is complete and the page has finished loading.
#
# Verify that the user has been redirected to the dashboard page by checking the URL or a specific element on the dashboard page.
#
# Ensure your script is synchronized with the page by handling dynamic content and AJAX responses.
#
# Make sure to handle any JavaScript alerts or popups if they appear during the login process.
#
# Questions for this assignment
# You are tasked with automating the login process for a web application that uses JavaScript and AJAX to submit form data and display results dynamically.
# The login page has an AJAX-based login mechanism where, after submitting credentials, the page shows a loading spinner until the response is received from the server.
# The user is redirected to the dashboard page upon successful login. Your task is to write a Selenium automation script that handles JavaScript and AJAX interactions properly.


driver = webdriver.Chrome()
driver.maximize_window()

try:
    # 1. Go to login page
    driver.get("https://practice.expandtesting.com/login")

    # 2. Wait for username/password fields
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    driver.find_element(By.NAME, "username").send_keys("practice")
    driver.find_element(By.NAME, "password").send_keys("SuperSecretPassword!")

    # 3. Submit login
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # 4. (Occasionally) Wait for spinner (replace selector if needed)
    try:
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".spinner"))
        )
    except TimeoutException:
        pass  # spinner may not always appear

    # 5. Verify redirect to secure/dashboard page
    WebDriverWait(driver, 10).until(
        EC.url_contains("/secure")
    )
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".success"))
    )
    print("✅ Login successful")

    # 6. (Optional) Handle JS alert
    try:
        alert = WebDriverWait(driver, 3).until(EC.alert_is_present())
        print("Alert appeared:", alert.text)
        alert.accept()
    except TimeoutException:
        pass

except TimeoutException:
    print("❌ Timeout occurred, login may have failed.")

finally:
    sleep(3)
    driver.quit()
