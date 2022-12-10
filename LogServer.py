import socket
import os
import glob
import time
import shutil

def filetransfer():
    s = socket.socket()
    host = socket.gethostname()
    port = 8080
    s.bind((host, port))
    s.listen(1)
    #print(host)
    print("waiting for any incoming connections..")
    conn, addr = s.accept()
    print(addr, "Has connected to the network")

    os.chdir(r"C:\Users\Isuru\Desktop\Test\Logs")
    #directory=os.getcwd()
    #print(directory)
    list_of_files = glob.glob(r'*.txt') # * means all if need specific format then *.csv.
    latest_file = min(list_of_files, key=os.path.getctime)
    filename = latest_file
    file = open(filename, 'rb')
    file_data = file.read(1024)
    conn.send(file_data)

    file.close()


    print("Data has been transmitted succesfully")

    new_path = r'C:\Users\Isuru\Desktop\Test\Logs\Sent' 
    shutil.move(filename, new_path)



