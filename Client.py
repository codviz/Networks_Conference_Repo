# echo-client.py

import socket

HOST = "127.0.0.1"
PORT = 65432  

Hello = bytes('Hello', encoding = 'ascii')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data_string = input("Guess A Number Between 1 and 100 (enter -1 to quit at anytime): ")
    data = bytes(data_string, encoding = 'ascii')
    s.sendall(data)
    data = s.recv(1024)

print(f"Received {data!r}")
