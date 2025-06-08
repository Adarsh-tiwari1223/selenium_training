from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Maximize browser window
driver.maximize_window()

# Navigate to example.com
driver.get("https://www.example.com")

# Wait for page to load
time.sleep(2)

# Locate elements using different methods
element_by_tag = driver.find_element(By.TAG_NAME, "h1")  # Method 1: Tag Name
element_by_css = driver.find_element(By.CSS_SELECTOR, "p")  # Method 2: CSS Selector
element_by_xpath = driver.find_element(By.XPATH, "//a")  # Method 3: XPath

# Print their text
print("H1 Text:", element_by_tag.text)
print("Paragraph Text:", element_by_css.text)
print("Link Text:", element_by_xpath.text)

# Take screenshot
driver.save_screenshot("example_page.png")

# Close the browser
driver.quit()
