import undetected_chromedriver as uc
import time

options = uc.ChromeOptions()
# options.add_argument("--headless")  # Optional for headless deployment

driver = uc.Chrome(options=options)
driver.get("https://www.messenger.com/")

input("Press Enter to exit...")