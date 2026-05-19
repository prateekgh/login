from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Launch Chrome normally (NOT headless)
from selenium.webdriver.chrome.options import Options

import yaml

# Load YAML file
with open("secrets.yaml", "r") as file:
    data = yaml.safe_load(file)

password = data["password"].get("rigohr")
email = data["password"].get("email")
    
chrome_options = Options()
chrome_options.add_argument("--headless=new") 
chrome_options.add_argument("--no-sandbox")
# Run in headless mode
driver = webdriver.Chrome(options=chrome_options)

# Open website
driver.get("https://app.rigohr.com")
time.sleep(2)


# Find the email input by its ID and fill it
email_input = driver.find_element(By.ID, "email-input")
email_input.clear()  # Clear any pre-filled text
email_input.send_keys(email)  
time.sleep(1)  # Wait for 5 seconds to allow the page to load
# Click Continue button
continue_button = driver.find_element(By.ID, "sign-btn")
continue_button.click()

# Wait to see next page
time.sleep(1)
# Fill password
password_input = driver.find_element(By.ID, "password-input")
password_input.send_keys("logintocontinue")

# Click sign in button again
# Click Log in
login_btn = driver.find_element(By.ID, "login-btn")
login_btn.click()

# Wait after login
time.sleep(2)


try:
    # Wait until greeting text appears
    greeting = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//p[contains(text(),'Hi')]")
        )
    )

    # Get text
    greeting_text = greeting.text
    print("Greeting found:", greeting_text)

    # Check if correct user
    if "Prateek Pudasainee" in greeting_text:

                # Click "Keep Working"
        button = driver.find_element(
            By.XPATH,
            "//a[contains(text(),'Keep Working') or contains(text(),'HR')]"
        )

        button.click()

        print("Clicked Keep Working or portal link")

    else:
        print("Different user detected")

except Exception as e:
    print("Greeting or button not found:", e)
    
    
clock_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((
        By.XPATH,
        "//button[contains(.,'Clock In') or contains(.,'Clock Out')]"
    ))
)


# Print the button text
print("Button text found:", clock_button.text)

# clock_button.click()

time.sleep(2)

driver.quit()

