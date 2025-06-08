from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://example.com')
# button = driver.find_element(By.ID,'submit-button')
# button.click()
link = driver.find_element(By.LINK_TEXT,'More information...')
link.click()
driver.quit()