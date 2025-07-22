from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Initialize Chrome driver
driver = webdriver.Chrome()

file_path = os.path.abspath('page/index.html')         # Get absolute path
file_url = 'file:///' + file_path.replace('\\', '/')   # Convert to file URL
driver.get(file_url)                                   # Load local HTML page

# Open the test page
driver.get(file_path)

# Attempt to interact with an element WITHOUT wait
try:
    element = driver.find_element(By.ID, 'dynamic-element')
    element.click()
except Exception as e:
    print(f"Error Without Wait: {e}")

# Introduce implicit wait
driver.implicitly_wait(10)

try:
    element = driver.find_element(By.ID, 'dynamic-element')
    element.click()
    print("Element clicked with implicit wait")
except Exception as e:
    print(f"Error With Implicit Wait: {e}")

# Optional: pause to see result
time.sleep(2)

# Clean up
driver.quit()
