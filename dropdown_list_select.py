import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


class DemoQADropdownPage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("https://demoqa.com/select-menu")
        time.sleep(2)

    # ✅ 1. Old Style Single Select Dropdown
    def select_old_style_option(self, visible_text):
        select_element = self.driver.find_element(By.ID, "oldSelectMenu")
        select = Select(select_element)
        select.select_by_visible_text(visible_text)
        print(f"Old Style: Selected '{visible_text}'")
        time.sleep(1)

    # ✅ 2. Standard Multi-Select Dropdown (with multiple)
    def select_standard_multi(self, *options):
        select_element = self.driver.find_element(By.ID, "cars")
        select = Select(select_element)

        if not select.is_multiple:
            raise Exception("Dropdown does not support multiple selection")

        for option in options:
            select.select_by_visible_text(option)
            print(f"Standard Multi: Selected '{option}'")
            time.sleep(0.5)

    def deselect_by_text(self, option_text):
        select = Select(self.driver.find_element(By.ID, "cars"))
        select.deselect_by_visible_text(option_text)
        print(f"Standard Multi: Deselected '{option_text}'")
        time.sleep(0.5)

    def deselect_all(self):
        select = Select(self.driver.find_element(By.ID, "cars"))
        select.deselect_all()
        print("Standard Multi: Deselected all options")
        time.sleep(0.5)


# ✅ Fixture: Setup and teardown
@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


# ✅ Test: Old Style Dropdown
def test_old_style_dropdown(driver):
    dropdown = DemoQADropdownPage(driver)
    dropdown.open_page()
    dropdown.select_old_style_option("Purple")

    selected = driver.find_element(By.ID, "oldSelectMenu").get_attribute("value")
    assert selected != "", "Old Style: No option was selected"


# ✅ Test: Standard Multi-Select Dropdown
def test_standard_multi_select(driver):
    dropdown = DemoQADropdownPage(driver)
    dropdown.open_page()

    dropdown.select_standard_multi("Volvo", "Opel", "Audi")
    dropdown.deselect_by_text("Volvo")
    dropdown.deselect_all()
