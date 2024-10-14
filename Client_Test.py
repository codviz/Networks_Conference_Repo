import socket
from threading import Thread
import os

class Client:

    def __init__(self, HOST, PORT):
        self.socket = socket.socket()
        self.socket.connect((HOST,PORT))
        self.name = input("Enter your name: ")

        self.talk_to_server()

    def talk_to_server(self):
        self.socket.send(self.name.encode())
        Thread(target = self.send_message).start()
        self.recieve_message()
    
    def send_message(self):
        while True:
            client_input = input("Guess A Number 0-3: ")
            client_message = self.name + ": " + client_input
            self.socket.send(client_message.encode()) 
    
    def recieve_message(self):
        pass

if __name__ == "__main__":
    Client('127.0.0.1', 7632)