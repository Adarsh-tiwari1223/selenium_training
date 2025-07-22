from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Initialize the WebDriver
driver = webdriver.Chrome()  # Make sure chromedriver is installed and in PATH
driver.maximize_window()

# Step 2: Open a webpage
driver.get("https://www.google.com")
time.sleep(2)

# Open a new tab using JavaScript
driver.execute_script("window.open('https://www.bing.com');")
time.sleep(2)

# Step 3: Switch to the new tab
windows = driver.window_handles
driver.switch_to.window(windows[1])
time.sleep(2)

# Step 4: Perform actions in the new tab
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium WebDriver")
search_box.submit()
time.sleep(3)

# Step 5: Switch back to the original tab
driver.switch_to.window(windows[0])
time.sleep(2)

# Step 6: Close all tabs/windows
driver.quit()
