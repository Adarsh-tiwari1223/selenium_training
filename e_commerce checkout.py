from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# === Step 1: Initialize WebDriver ===
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # === Step 2: Navigate to E-commerce Site ===
    driver.get("https://example-ecommerce-site.com")  # Replace with real site
    time.sleep(2)

    # === Step 3: Go to Login Page ===
    login_link = driver.find_element(By.LINK_TEXT, "Login")
    login_link.click()
    time.sleep(2)

    # === Step 4: Fill and Submit Login Form ===
    driver.find_element(By.ID, "email").send_keys("testuser@example.com")
    driver.find_element(By.ID, "password").send_keys("password123")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    # === Step 5: Navigate to Product Listing Page ===
    driver.get("https://example-ecommerce-site.com/products")  # Replace with real product page URL
    time.sleep(2)

    # === Step 6: Choose a Product and View Details ===
    product = driver.find_element(By.CSS_SELECTOR, ".product-item a")  # Adjust selector to your site
    product.click()
    time.sleep(2)

    # === Step 7: Add Product to Cart ===
    driver.find_element(By.ID, "add-to-cart").click()
    time.sleep(2)

    # === Step 8: Go to Checkout Page ===
    driver.get("https://example-ecommerce-site.com/cart")
    time.sleep(2)
    driver.find_element(By.ID, "checkout-button").click()
    time.sleep(3)

    print("✅ Script completed successfully!")

except Exception as e:
    print("Error occurred:", e)

finally:
    driver.quit()
