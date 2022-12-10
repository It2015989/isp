import socket
import os

s = socket.socket()
host = 'DESKTOP-J0C9MTF'
port = 8080
s.connect((host, port))
print("connected...")

os.chdir(r'C:\1)SLIIT\3rd Year\2nd Semester\Information Security Project\Tests\Transfer\Received')


filename = input(str("Please enter a filename for the incoming file  :"))
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("file has beeen received successfully.")
