import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time

options = uc.ChromeOptions()
# options.add_argument("--headless")  # Optional for headless deployment

driver = uc.Chrome(options=options)

load_dotenv()
EMAIL = os.getenv("MESSENGER_EMAIL")
PASSWORD = os.getenv("MESSENGER_PASSWORD")

driver.get("https://www.messenger.com/")

time.sleep(3)
driver.find_element(By.ID, "email").send_keys(EMAIL)
driver.find_element(By.ID, "pass").send_keys(PASSWORD)
driver.find_element(By.ID, "pass").send_keys(Keys.RETURN)

input("Press Enter to exit...")