from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://google.co.in')

text_field = driver.find_element(By.ID,'APjFqb')

text_field.send_keys('Naredra Modi')
time.sleep(1)