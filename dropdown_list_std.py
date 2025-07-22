import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class DemoQADropdownPage:
    def __init__(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def open_page(self):
        self.driver.get("https://demoqa.com/select-menu")
        time.sleep(2)

    def select_old_style_option(self, visible_text):
        select_element = self.driver.find_element(By.ID, "oldSelectMenu")
        from selenium.webdriver.support.ui import Select
        select = Select(select_element)
        select.select_by_visible_text(visible_text)
        time.sleep(1)

    def multi_select_values(self, *options):
        # Click the multi-select input box
        input_box = self.driver.find_element(By.XPATH, "//div[contains(@class,'css-1hwfws3')]//div[contains(text(),'Select...')]")
        input_box.click()
        time.sleep(1)

        for option in options:
            option_element = self.driver.find_element(By.XPATH, f"//div[contains(@class,'menu')]//div[text()='{option}']")
            option_element.click()
            time.sleep(1)

    def close_browser(self):
        time.sleep(2)
        self.driver.quit()


# ✅ Usage
if __name__ == "__main__":
    dropdown = DemoQADropdownPage()
    dropdown.open_page()
    dropdown.select_old_style_option("Purple")
    dropdown.multi_select_values("Green", "Blue", "Black")
    dropdown.close_browser()
