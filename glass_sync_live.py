import cv2
import numpy as np
import mss
import time
from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID


def find_window_bounds(title_contains):
    windows = CGWindowListCopyWindowInfo(
        kCGWindowListOptionOnScreenOnly,
        kCGNullWindowID
    )

    for w in windows:
        name = w.get("kCGWindowName", "")
        if name and title_contains in name:
            bounds = w["kCGWindowBounds"]
            return {
                "top": int(bounds["Y"]),
                "left": int(bounds["X"]),
                "width": int(bounds["Width"]),
                "height": int(bounds["Height"]),
            }

    return None


with mss.mss() as sct:
    while True:
        region = find_window_bounds("Messenger call")

        if not region:
            print("Messenger Call window not found...")
            time.sleep(1)
            continue

        screenshot = sct.grab(region)
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

        cv2.imshow("Messenger Feed", frame)

        if cv2.waitKey(1) == 27:
            break

cv2.destroyAllWindows()