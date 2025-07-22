import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AlertHandling:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_confirm")
        self.driver.maximize_window()

    def handle_alert(self, accept=True):
        driver = self.driver
        try:
            # Switch to the iframe that contains the button
            driver.switch_to.frame(driver.find_element(By.ID, "iframeResult"))
            print("Switched to iframe.")

            # Click the button to trigger the alert
            driver.find_element(By.XPATH, "//button[text()='Try it']").click()
            print("Button clicked, waiting for alert.")

            # Wait for the alert to appear
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            print("Alert appeared.")

            # Accept or dismiss the alert based on input
            if accept:
                alert.accept()
                print("Alert accepted.")
            else:
                alert.dismiss()
                print("Alert dismissed.")

            time.sleep(3)  # Just to observe the result briefly

        except Exception as e:
            print(f"Error handling alert: {e}")

        finally:
            driver.quit()
            print("Browser closed.")

if __name__ == "__main__":
    handler = AlertHandling()
    handler.handle_alert(accept=True)  # Change to False to click "Cancel"

# START
#   │
#   ▼
# Initialize Chrome WebDriver
#   │
#   ▼
# Open W3Schools Confirm Box Demo Page
#   │
#   ▼
# Maximize Browser Window
#   │
#   ▼
# switch_to.frame("iframeResult")
#   │
#   ▼
# Find and Click "Try it" Button (Triggers JS Confirm Alert)
#   │
#   ▼
# Wait until Alert Appears (EC.alert_is_present)
#   │
#   ▼
# Is `accept=True`?
#  ┌──────────────┐
#  │              │
# Yes             No
#  │              │
#  ▼              ▼
# alert.accept()  alert.dismiss()
#   │              │
#   └──────┬───────┘
#          ▼
# Wait for 3 seconds (time.sleep)
#          ▼
# driver.quit()
#          ▼
# END
