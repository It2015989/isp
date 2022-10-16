
# importing pyautogui random and time
# libraries
import pyautogui
import mss
import random
import time
from PIL import Image  # Will need to make sure PIL is installed


def take_screenshots():  # Running the while loop for infinite time
    with mss.mss() as mss_instance:
        monitor = mss_instance.monitors[0]
        screenshot = mss_instance.grab(monitor)

        file_name = time.strftime("%Y%m%d-%H%M%S")+".png" #cerating file name
        # Convert to PIL.Image
        img = Image.frombytes("RGB", screenshot.size,
                              screenshot.bgra, "raw", "BGRX")
        img.save(
            f"C:\\1)SLIIT\\3rd Year\\2nd Semester\\Information Security Project\\Tests\\Test 2\\Screenshots\\{file_name}") #save capture screenshot
