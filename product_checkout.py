from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Step 1: Open browser and navigate to the e-commerce website
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com/products")

# Step 2: Search for the product "chocolate"
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "search"))
)
search_box.send_keys("Shirt")

# Click on the search button
driver.find_element(By.ID, "submit_search").click()

# Step 3: Wait for search results and add first product to cart
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product-image-wrapper"))
    )
    # Scroll to the first product
    driver.execute_script("window.scrollBy(0, 300);")
    sleep(2)

    # Hovering over product and clicking "Add to cart"
    first_product = driver.find_element(By.XPATH, "(//a[contains(text(),'Add to cart')])[1]")
    first_product.click()

    # Step 4: Proceed to cart (click 'View Cart')
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//u[text()='View Cart']"))
    ).click()

    # Step 5: Proceed to Checkout
    print("At the Cart Page. You can now proceed to checkout manually or automate login flow.")
except Exception as e:
    print("Something went wrong:", e)

# Optional sleep to view results
sleep(5)
driver.quit()
