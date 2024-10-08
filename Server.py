# echo-server

import socket
import random

HOST = "127.0.0.1"
PORT = 65432
guess = str(random.randint(0,10))
correct_message = bytes("You Got It!, Generating New Number... ", encoding = 'ascii')
incorrect_message = bytes("Wrong Guess!", encoding = 'ascii')
severing_message = bytes("Ending Connection...", encoding = 'ascii')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    while True:
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            data = conn.recv(1024)
            if data == bytes(guess, encoding = 'ascii'):
                conn.sendall(correct_message)
                guess = str(random.randint(0,10))
            elif data == bytes('-1', encoding = 'ascii'):
                conn.sendall(severing_message)
                break
            else:
                conn.sendall(incorrect_message)
