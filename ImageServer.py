import socket
import os
import glob
import shutil

def sendimage():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 8081
    s.bind((host, port))
    s.listen(1)
    print(host)
    print("waiting for any incoming connections..")
    conn, addr = s.accept()

    os.chdir(r"C:\Users\Isuru\Desktop\Test\Screenshot")

    list_of_files = glob.glob(r'*.png') # * means all if need specific format then *.csv.
    latest_file = min(list_of_files, key=os.path.getctime)
    filename = latest_file
    file = open(filename, 'rb')
    image_data = file.read(2048)
    while image_data:
        conn.send(image_data)
        image_data = file.read(2048)

    file.close()
    conn.close()

    new_path = r'C:\Users\Isuru\Desktop\Test\Screenshot\Sent' 
    shutil.move(filename, new_path)