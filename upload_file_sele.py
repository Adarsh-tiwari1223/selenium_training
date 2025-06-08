from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://google.co.in')

file_input = driver.find_element(By.ID,'file-upload-id')

file_input.send_keys('Path/to/your/file')
time.sleep(1)
driver.quit()