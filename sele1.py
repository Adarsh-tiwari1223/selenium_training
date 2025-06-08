from selenium import webdriver
from selenium.webdriver.common.by import By
import time  # For simple delay

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Wait for page to load
time.sleep(2)  # Better: use WebDriverWait in real projects

# Accept cookies/pop-ups if needed (Google shows them sometimes)

# Search for "Selenium"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
search_box.submit()

# Wait for results to load
time.sleep(2)

# Click the link containing 'Selenium'
driver.find_element(By.PARTIAL_LINK_TEXT, 'Selenium').click()

# Print the title of the new page
print(driver.title)

# Close the browser
driver.quit()
