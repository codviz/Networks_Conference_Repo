# echo-client.py

import socket

HOST = "127.0.0.1"
PORT = 65432  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Sending Data...")
    s.sendall(b"My Name")
    data = s.recv(1024)

print(f"Received {data!r}")