import socket, threading
import random

class Server:

    def __init__(self):

        LISTENING_PORT = 12000
        self.clients = []
        
        try:
            socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_instance.bind(('', LISTENING_PORT))
            socket_instance.listen()

            print('Server running!')
            
            while True:

                socket_connection, address = socket_instance.accept()
                self.clients.append(address)
                threading.Thread(target= self.handle_user_connection, args=[socket_connection, address]).start()
                
        
        except Exception as e:
            print(f'An error has occurred when instancing socket: {e}')
            socket_connection.close()

    def handle_user_connection(self, connection: socket.socket, address: str):

        random_number = random.randint(0,4)
        print(f"Connected From {address}")
        print(f"Random Number For {address} is {random_number}")
        print(f"Server Currently Has {len(self.clients)} Connections")
        print("..")

        while True:

            try:
                msg = connection.recv(1024)
                if (msg.decode() == str(random_number)):
                    connection.send(f"You Got It! \nRegenarating Number! \n..".encode())
                    random_number = random.randint(0,4)
                    print(f"Random Number For {address} is {random_number}")

                elif (msg.decode()) == "Quit":
                    self.clients.remove(address)
                    print(f"{address} Has Disconnected")
                    print(f"Server Currently Has {len(self.clients)} Connections")
                    connection.send(f"Goodbye!".encode())
                    connection.close()
                    break

                else:
                    connection.send(f"Not Quite... \nGuess A Number Between 0 and 4, Type 'Quit' To Disconnect From Server: \n..".encode())

            except Exception as e:
                print(f'Error to handle user connection: {e}')
                self.clients.remove(address)
                print(f"{address} Has Disconnected")
                print(f"Server Currently Has {len(self.clients)} Connections")
                break

    
    


if __name__ == "__main__":
    server = Server()
