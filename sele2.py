from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.get("https://en.wikinews.org/wiki/Special:Search?go=Go&search=india+news&ns0=1&ns14=1")

time.sleep(3)  # Wait for results to load

# Grab all result titles
titles = driver.find_elements(By.CSS_SELECTOR, 'ul.mw-search-results li.mw-search-result a')

for index, title in enumerate(titles):
    print(f"{index+1}. {title.text} - {title.get_attribute('href')}")

driver.quit()
