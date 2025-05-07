import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time
from urllib.parse import urlparse
from datetime import datetime
import requests

# Media download function
def download_media(src_url):
    try:
        # Create a filename based on timestamp + original filename
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        parsed_url = urlparse(src_url)
        filename = os.path.basename(parsed_url.path)
        ext = filename.split('.')[-1] if '.' in filename else 'bin'
        full_filename = f"media_{timestamp}.{ext}"

        # Download the file
        response = requests.get(src_url, stream=True)
        response.raise_for_status()

        # Save it locally
        with open(full_filename, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"✅ Downloaded: {full_filename}")
    except Exception as e:
        print(f"⚠️ Failed to download {src_url}: {e}")

# Set up Chrome
options = uc.ChromeOptions()
# options.add_argument("--headless")  # Optional for headless deployment
driver = uc.Chrome(options=options)

# Load environment variables
load_dotenv()
EMAIL = os.getenv("MESSENGER_EMAIL")
PASSWORD = os.getenv("MESSENGER_PASSWORD")

# Navigate to Messenger
driver.get("https://www.messenger.com/")
time.sleep(3) # Wait for page to load

# Enter login credentials and submit 
driver.find_element(By.ID, "email").send_keys(EMAIL)
driver.find_element(By.ID, "pass").send_keys(PASSWORD)
driver.find_element(By.ID, "pass").send_keys(Keys.RETURN)
time.sleep(5) # Wait for page to load

# Find all video and image elements
videos = driver.find_elements(By.TAG_NAME, "video")
images = driver.find_elements(By.TAG_NAME, "img")

# Load initial media sources on first page load ---
initial_media = driver.find_elements(By.TAG_NAME, "video") + driver.find_elements(By.TAG_NAME, "img")
seen_sources = set()
for element in initial_media:
    src = element.get_attribute("src")
    if src:
        seen_sources.add(src)
print(f"Initialized with {len(seen_sources)} existing media sources.")

# Monitor for new media appearing
while True:
    media_elements = driver.find_elements(By.TAG_NAME, "video") + driver.find_elements(By.TAG_NAME, "img")

    for element in media_elements:
        src = element.get_attribute("src")
        if src and src not in seen_sources:
            seen_sources.add(src)
            print("New media detected")
            download_media(src)
    time.sleep(3)

input("Press Enter to exit...") # Pause