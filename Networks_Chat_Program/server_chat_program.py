import socket, threading
import random

class Server:

    def __init__(self):

        LISTENING_PORT = 12000
        self.clients = []
        self.client_usernames = []
        self.commands = ["<Client-Dir> - Gives List Of Client Usernames Connected To Server"
                         ]
        
        try:
            socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_instance.bind(('', LISTENING_PORT))
            socket_instance.listen()

            print('Server running!')
            
            while True:

                socket_connection, address = socket_instance.accept()
                threading.Thread(target= self.handle_user_connection, args=[socket_connection, address]).start()
                
        
        except Exception as e:
            print(f'An error has occurred when instancing socket: {e}')
            socket_connection.close()

    def handle_user_connection(self, connection: socket.socket, address: str):
        connection.send(str(self.commands).encode())
        while True:

            msg = connection.recv(1024)
            client_username = msg.decode()
            if client_username in self.client_usernames:
                connection.send("INVALID_USERNAME".encode())
            else:
                connection.send("VALID_USERNAME".encode())
                self.clients.append([client_username, connection])
                self.client_usernames.append(client_username)
                break
            

        while True:

            try:
                
                msg = connection.recv(1024)
                if (msg.decode() == "<Client-Dir>"):
                    connection.send(str(self.client_usernames).encode())
                else:
                    connection.send("ERROR: Invalid Command".encode())

            except Exception as e:
                print(f'Error to handle user connection: {e}')
                break


    
    


if __name__ == "__main__":
    server = Server()
