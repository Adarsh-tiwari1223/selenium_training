from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()

driver.get('https://example.com')
driver.find_element(By.ID,'trigger-alert').click()
alert = driver.switch_to.alert

alert.accept()