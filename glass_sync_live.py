import cv2
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Attach to existing Chrome
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)


# Find Messenger tab explicitly
messenger_handle = None

for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if "messenger" in driver.current_url.lower():
        messenger_handle = handle
        break

if messenger_handle is None:
    raise Exception("Messenger tab not found")

driver.switch_to.window(messenger_handle)

print("Messenger tab found. Streaming...")

while True:
    # This captures the TAB directly via Chrome DevTools
    png = driver.get_screenshot_as_png()

    frame = cv2.imdecode(np.frombuffer(png, np.uint8), cv2.IMREAD_COLOR)

    cv2.imshow("Messenger Feed", frame)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()