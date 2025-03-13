import random
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def generate_random_number():
  return random.randint(1, 2573157538607026564968244111304175730063056983979442319613448069811514699875)

def check_key_page(random_number):
  url = f"https://privatekeys.pw/keys/bitcoin/{random_number}"
  search_html = '<span class="final " data-bs-toggle="tooltip" data-bs-original-title="Total balance"><i class="cf cf-btc" aria-hidden="true"></i> 0</span>'

  chrome_options = Options()
  chrome_options.add_argument("--headless")  # Run Chrome in the background

  driver = webdriver.Chrome(options=chrome_options)  # Use the options
  driver.get(url)

  try:
    # Wait for the specific element to be present
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'span.final'))
    )
    page_content = driver.page_source


    if search_html in page_content:
      print(f"Balance is 0 :(: {random_number}")
    else:
      print(f"OMG!!! DID YOU FIND GOLD? OPEN PAGE: {random_number}")
      while True:
          os.system(f"afplay /System/Library/Sounds/Funk.aiff")
  finally:
    driver.quit()

# Search for the HTML 400 times
for _ in range(400):
  random_number = generate_random_number()
  try:
    check_key_page(random_number)
  except:
    print("Something went wrong with the request")
