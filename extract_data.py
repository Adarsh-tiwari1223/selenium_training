from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the target URL
driver.get("https://demoqa.com/dynamic-properties")

# Optional: wait for a specific element to be present (example usage)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "someElementId"))
    )
    print("Element found:", element.text)
except:
    print("Element not found within the time limit.")

# Sleep for a while if needed
sleep(5)

# Close the driver
driver.quit()
