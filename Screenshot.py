# importing random and time libraries
import pyautogui
import mss
import random
import time
from PIL import Image


def take_screenshots():  # Running the while loop for infinite time
    with mss.mss() as mss_instance:
        monitor = mss_instance.monitors[0]
        screenshot = mss_instance.grab(monitor)

        file_name = time.strftime("%Y%m%d-%H%M%S")+".png"
        # Convert to PIL.Image
        img = Image.frombytes("RGB", screenshot.size,
                              screenshot.bgra, "raw", "BGRX")
        img.save(f"C:\\Users\\Isuru\\Desktop\\Test\\Screenshot\\{file_name}")
        time.sleep(5)
