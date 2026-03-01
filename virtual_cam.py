import pyvirtualcam
import numpy as np
import cv2

width = 1280
height = 720
fps = 30

with pyvirtualcam.Camera(width=width, height=height, fps=fps, backend="obs") as cam:
    print("Publishing to OBS Virtual Camera...")

    while True:
        frame = np.zeros((height, width, 3), dtype=np.uint8)

        # Example content
        cv2.putText(frame, "GlassSync Live",
                    (100, 200),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    2,
                    (0, 255, 0),
                    4)

        cam.send(frame)
        cam.sleep_until_next_frame()