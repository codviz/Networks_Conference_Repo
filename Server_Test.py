import socket
from threading import Thread
from random import randint

class Server:

    Clients = []
    number_guess = randint(0,3)

    def __init__(self, HOST, PORT):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((HOST, PORT))
        print("Waiting for connections... ")
        self.socket.listen(5)
    
    def listen(self):
        client_socket, address = self.socket.accept()
        print("Connection from: " + str(address))

        client_name = client_socket.recv(1024).decode()
        client = {'client_name': client_name, 'client_socket': client_socket}

        print(client_name + " has entered the game")

        Server.Clients.append(client)
        Thread(target = self.handle_new_client, args = (client,)).start()

    def handle_new_client(self, client):
        client_name = client['client_name']
        client_socket = client['client_socket']
        while True:
            client_message = client_socket.recv(1024).decode()
            if client_message == (client_name +": " + str(Server.number_guess)):
                print("Correct Guess!")
                break
            else:
                print("Not Quite!")

if __name__ == '__main__':
    server = Server('127.0.0.1', 7632)
    server.listen()

