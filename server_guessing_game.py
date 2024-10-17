import socket, threading
import random

random_number = random.randint(0,4)

def handle_user_connection(connection: socket.socket, address: str):

    while True:
        try:
            msg = connection.recv(1024)
            if (msg.decode() == str(random_number)):
                connection.send("you got it!".encode())
                connection.send("regenerating number!".encode())
            else:
                connection.send("not quite... ".encode())
                connection.send("Guess A Number Between 0 and 4, Type 'quit' to exit: ".encode())
        except Exception as e:
            print(f'Error to handle user connection: {e}')
            break

def server():

    LISTENING_PORT = 12000
    
    try:
        socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_instance.bind(('', LISTENING_PORT))
        socket_instance.listen()

        print('Server running!')
        
        while True:

            socket_connection, address = socket_instance.accept()
            threading.Thread(target=handle_user_connection, args=[socket_connection, address]).start()

    except Exception as e:
        print(f'An error has occurred when instancing socket: {e}')


if __name__ == "__main__":
    server()