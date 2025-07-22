from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from time import sleep

# Setup headless (optional)
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.maximize_window()

try:
    
    driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/")

    
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe.demo-frame"))
    )

    
    # Example: Fill two text fields (assuming IDs "firstname" and "lastname")
    driver.find_element(By.ID, "firstname").send_keys("Shrey")
    driver.find_element(By.ID, "lastname").send_keys("Tiwari")

    # Example dropdown (if present)
    Select(driver.find_element(By.ID, "country")).select_by_visible_text("India")

    # Submit the form (assuming button ID "submitBtn")
    driver.find_element(By.ID, "submitBtn").click()

    
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("Alert says:", alert.text)
    alert.accept()

    
    driver.switch_to.default_content()

    
    driver.get("https://www.globalsqa.com/demo-site/tooltip/")


    hover_elem = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".tooltip .tooltiptext"))
    )
    inner = driver.find_element(By.XPATH, "//label[text()='Country']/following-sibling::select")
    ActionChains(driver).move_to_element(inner).perform()

    tooltip = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".tooltip .tooltiptext"))
    )
    print("Tooltip text:", tooltip.text)

except TimeoutException as e:
    print("A timeout occurred:", e)

finally:
    sleep(3)
    driver.quit()
