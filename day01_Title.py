from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time  # For simple delay

class Calendar:
    def __init__(self):
        self.driver = None

    def open_yatra(self):
        self.driver = open_yatra()

    def select_date(self, date):
        if self.driver is None:
            raise Exception("Driver not initialized. Call open_yatra() first.")
        select_date(self.driver, date)

def open_yatra():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()
    # Open the Yatra website
    driver.get("https://www.yatra.com/")
    
    # Wait for the page to load
    time.sleep(2)  # Better: use WebDriverWait in real projects
    return driver

def select_date(driver, date):
    # Click on the date picker
    date_picker = driver.find_element(By.ID, "BE_flight_origin_date")
    date_picker.click()
    
    # Wait for the date picker to open
    time.sleep(1)  # Better: use WebDriverWait in real projects
    
    # Select the date
    date_element = driver.find_element(By.XPATH, f"//td[@data-date='{date}']")
    date_element.click()

# Wait for page to load
time.sleep(2)  # Better: use WebDriverWait in real projects
