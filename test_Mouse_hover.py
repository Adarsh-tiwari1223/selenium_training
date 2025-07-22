import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestHover:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.w3schools.com/cssref/tryit.php?filename=trycss_sel_hover_dropdown")
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()


    def test_hover(self):
        driver = self.driver

        wait = WebDriverWait(driver, 5)
        try:

            # ✅ Switch to the iframe before interacting with elements inside it
            iframe = wait.until(EC.presence_of_element_located((By.ID, "iframeResult_0")))
            driver.switch_to.frame(iframe)

            # Locate the dropdown element
            dropdown = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Dropdown Link")))

            # Hover over the dropdown
            ActionChains(driver).move_to_element(dropdown).perform()

            # Wait for Link 1 to appear
            link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Link 1")))
            link.click()
            print("Hover successful. Found:", link.text)

            time.sleep(2)  # Just for visibility
        except Exception as e:
            print(e)


