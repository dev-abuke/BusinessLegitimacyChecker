from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the page
driver.get("https://etrade.gov.et/")

# Wait for the page to load completely
driver.implicitly_wait(10)  # seconds

# Find the TIN input field and enter a TIN number
tin_input = driver.find_element(By.ID, "tin")
tin_input.send_keys("123456789")

# Find the search button and click it
search_button = driver.find_element(By.XPATH, '//a[contains(@href, "/business-license-checker?tin=")]')
search_button.click()

# Wait for the search results to load
driver.implicitly_wait(10)  # seconds

# Assuming results are loaded in a new element or page, scrape necessary data
# This is a placeholder: you would adjust the selector based on actual results layout
results = driver.find_element(By.ID, 'results')  # Example ID
print(results.text)

# Close the browser
driver.quit()